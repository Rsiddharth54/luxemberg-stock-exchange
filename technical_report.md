# 📌***Techinical Report***

## 1. Project goals

This API is a FastAPI-based application designed to retrieve, process, and compare data from the Transition Pathway Initiative Centre (TPI). It provides a fully functional API for delivering data from key assessment frameworks developed by the TPI Centre, including ASCOR, Carbon Performance, and Management Quality. 
Our team’s specific objective is to collaborate with clients from the Luxembourg Stock Exchange to enhance existing endpoints and develop new ones tailored to their needs, including endpoints for serving both data and visual content.

--- 

## 2. Design decisions (and rationale, including rejected ideas)

### Carbon Performance Visualisation

- **Why Plotly?**  

  Plotly was the ideal choice for our carbon‐performance graphs because it lets us implement our entire visualization pipeline in Python with minimal boilerplate, while still producing static images on the server. In our design we needed:  
  1. **Layered fills** for the “1.5 °C”, “Below 2 °C” and “International Pledges” benchmark bands, Plotly’s `fill="tozeroy"/"tonexty"` makes it easy to implement.
  2. **Mixed line styles** — solid for historical data, dashed for projections, dotted for target trajectories are all configurable via simple `line` attributes.  
  3. **Markers** (the green 2030 target dot) without manual coordinate calculations.  
  4. **Single code path** for both JSON-serializable figure objects (for any future client-side use) and server-side PNG/JPEG exports (`fig.to_image()`), so we don’t maintain separate D3 or Matplotlib scripts.  
  5. **Legend & hover customization** — even though we currently serve static images, having hover/tooltips and legend toggling “built-in” in the figure definition means future front-end interactivity can be enabled simply by returning the figure’s JSON.  

We considered using Matplotlib (with Seaborn) for everything, but it would have needed a lot more code to get stacked translucent areas and multiple line styles, and it doesn’t export interactive JSON.



---
## 3. Methodology

### Carbon Performance Visualisation

  Endpoint wiring
  - **Path:**  
    `GET /company/{company_identifier}/carbon-performance-graph`
  - **Flow:**  
    1. Parse & validate query params in `cp_routes.py`  
    2. `get_company_carbon_intensity(...)` → structured `data`  
    3. `generate_carbon_intensity_graph(...)` → JSON or `StreamingResponse`  
  - **Response schema:**  
    - `application/json` → Plotly figure model  
    - `image/png` / `image/jpeg` → binary image  
  - **Query parameters & validation**  
    - `include_sector_benchmarks` (bool, default =true)  
    - `as_image` (bool, default =false)  
    - `image_format` (str, “png”|“jpeg”)  
    - `width` (int, 400–2000), `height` (int, 300–1200)  
    - `title` (optional string)  
    FastAPI/Pydantic enforces types, ranges and formats automatically.

1. **Data preparation**  
   - Load the corporate carbon intensity DataFrame (`cp_df`) and the sector benchmark DataFrame (`sector_bench_df`).  
   - Filter `cp_df` by the given ISIN or company name and select the row with the latest assessment cycle.

2. **Benchmark extraction**  
   - For each mitigation pathway (“1.5 °C”, “Below 2 °C”, “International Pledges”), read the corresponding `"years"` and `"values"` arrays from `sector_bench_df`.

3. **Company series**  
   - From the selected company row in `cp_df`, extract the reported `"years"` and `"values"`.  
   - Find the last year ≤ 2024 and split the series into:
     - `solid_pts` (years ≤ 2024)  
     - `dash_pts` (years ≥ 2024)

4. **Target parsing**  
   - Extracts ALL columns that end with a 4-digit year (e.g., "2013", "2014", ..., "2050") from the CP assessment data. Each year column contains the carbon intensity value for that specific year.

5. **Visualization generation**  
   In `CarbonPerformanceVisualizer.generate_carbon_intensity_graph`:
   ```python
   # a. Add stacked filled traces for each benchmark pathway
   # b. Add the sector mean (up to 2022) as a red line
   # c. Add the reported history (solid for historical, dashed for projected)
   # d. Add a green marker at 2030 if a target exists
   # e. Add the corporate target series as a dotted green line
   # f. Configure layout: title, axes labels, legend styling, hovermode
6. **Unit Test**
    Added 22 unit tets for the visualisation
    - **Carbon Intensity Data Endpoint Tests**  
    - **Success**: `/carbon-intensity/{company}` returns 200 and a valid dict for “vectren.”  
    - **Not Found**: non-existent company returns 404 (or 500 if unhandled).  
    - **By ISIN**: endpoint accepts an ISIN format and returns without unexpected errors.

  - **Carbon Performance Graph Endpoint Tests**  
    - **As Image (PNG)**: `?as_image=true&image_format=png` returns 200 with `image/png` header.  
    - **As JSON**: `?as_image=false` returns 200 and a dict containing `"data"` and/or `"layout"`.  
    - **Custom Dimensions**: `?width=800&height=400` reflects those values in the returned figure’s layout.  
    - **Custom Title**: `?title=Foo` sets the figure’s title (string or `{ "text": "Foo" }`).  
    - **With/Without Benchmarks**: toggles inclusion of benchmark traces.  
    - **JPEG Format**: `?image_format=jpeg` returns `image/jpeg`.  
    - **Not Found**: non-existent company returns 404.  
    - **Dimension Limits**: rejects out-of-range (`300×200`) with 422, accepts `400×300` and `2000×1200`.

  - **Carbon Intensity Utility Function Tests**  
    - Mocks `cp_df` and `sector_bench_df` to verify `get_company_carbon_intensity()` returns the expected structure: years, values, sector mean, benchmarks, units.

  - **Visualization Logic Tests**  
    - Mocks `CarbonPerformanceVisualizer.generate_carbon_intensity_graph` to confirm it’s called with correct parameters (title, width, height, format).

  - **Error Handling Tests**  
    - Invalid company identifiers produce the appropriate 404, 422, or 500 responses.  
    - Invalid graph parameters (e.g. bad dimensions) produce 422 errors.

  - **Integration Tests**  
    - Full workflow: retrieve intensity data, then graph JSON/image for the same company, asserting consistency.

  - **Fixture Tests**  
    - Latest CP response matches a saved fixture (10 companies, required fields).  
    - Company history for “vectren” matches fixture.  
    - CP alignment response for “AES” includes core years (2025, 2027, 2035, 2050).  
    - CP comparison for “AES” matches fixture structure (current vs previous assessment).


---
## 4. Client interaction

### **Reflection from First Meeting**

**Meeting Time:** 12th May, 15:15–15:45 BST  
**Meeting Goal:** Identifies client needs and defines the necessary steps to address them.

### **Key Questions Answered**

#### 1. What key use cases should this API support?  
(For example: listing metrics, company profiles, sector data, etc.)

- The goal is to help data users better filter and use the dataset for their own needs.
- The **primary endpoint** is **entity-level data** (Company or Country).
- This should be broken down into different methodologies:
  - **CP** and **MQ** for companies.
- Results should be served by entity with the associated metrics.
- Users should ideally be able to specify which metrics they're interested in (all or specific ones).  
  **Example:**  
  - All metrics for German companies.  
  - All level 4 MQ metrics and CP alignment for Chinese companies.

#### 2. Which datasets from the TPI website are we building against?  
(If multiple datasets are needed, how should the API handle interactions between them?)

- Focus: **CP** and **MQ** (potentially link with **ASCOR** and **Banking**, depending on scope and time).
- Ideally, datasets will be **linked by entity** and other identifiers.  
  **Example:**  
  - Link through the geography code to the ASCOR dataset, allowing users to download ASCOR indicators alongside companies headquartered in that jurisdiction.

#### 3. How will you query these endpoints?  
(What filters and parameters are required? How should the API handle missing/incomplete data?)

- The API should return a **“data not available”** or **relevant description** when data is missing.
- If a reason for missing data exists (e.g. insufficient company disclosure), it should be included in the response.

#### 4. Do you need chart images or raw data, or both?  
(If raw data is enough, which formats are preferred?)

- One of the **key goals** is to **include both graphs and underlying data** directly in the API.

### **List of Priorities After the Meeting**

1. Solve any remaining bugs that affect the rest of the work
2. Add filters for mass calls by region and sector.
3. Add the underlying CP assessment data for each company:
   - Use data from:
     - `CP Assessment.xlsx`
     - `CP Assessment Regional.xlsx`
     - Benchmarks from `Sector Benchmark.xlsx` (for Electric Utilities sector).
4. Use the data to create graphs on the website (see example at bottom of the page).
5. Add endpoints to serve **Banking data**.
6. Link datasets to allow:
   - Calling **ASCOR indicators** in a Country
   - Fetching companies headquartered in that country
7. Add other functionality as discussed and as time/interests allow, subject to **Jon's confirmation** (e.g. chatbot).

### **Reflection from Second Meeting**

**Meeting Time:** 19th May, 14:30 – 15:30 BST
**Meeting Goal:** Assesses current version and identifies specific areas for improvement.

---
## 5. System architecture
---
## 6. Evaluation results

### Carbon Performance Visualisation

All unit tests passed successfully. The generated graphs match those on the TPI website and have been approved by our clients.
---
## 7. Analysis
---
## 8. Limitations

### Carbon Performance Visualisation

Despite extensive validation, our sector mean line occasionally diverges from the one displayed on the TPI website. The original calculation is performed by a legacy Visuality function to which we have no source code access. Although we adjusted our implementation based on client feedback, some discrepancies still remain. We have requested more details from the data owners, but until we hear back, we defined our own sector mean calculation. Until then, slight differences in the sector mean line may persist. Additionally, certain assumptions such as the hard-coded 2024 cutoff for historical data and the fixed green dot at 2030remain in place and could limit flexibility for some use cases.


---
## 9. Conclusions