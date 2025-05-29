import pytest
import pandas as pd

from main import app

from fastapi.testclient import TestClient

from dotenv import load_dotenv
load_dotenv(dotenv_path=".env")

"""CONSTANTS

TODO: Create a config.py file to store these constants
"""

EXCEL_PATH = 'data/TPI_ASCOR_data_13012025/ASCOR_assessments_results.xlsx'

"""SETUP FIXTURES"""

@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture
def df_assessments():
    """Database dependency"""
    df_assessments = pd.read_excel(EXCEL_PATH)
    df_assessments['Publication date'] = pd.to_datetime(df_assessments['Publication date'], format='%d/%m/%Y')
    df_assessments['Assessment date'] = pd.to_datetime(df_assessments['Assessment date'], format='%d/%m/%Y')
    try:
        yield df_assessments
    finally:
        # Any cleanup if needed
        pass


"""FIXTURES WITH EXPECTED RESPONSES"""

# --------------------------------------------------------------------------
# Ascor endpoint fixtures
# --------------------------------------------------------------------------
@pytest.fixture
def expected_ascor_response():
    """Expected response structure for Ascor country-data endpoint with Canada, 2023 as example"""
    return {
    "country": "canada",
    "assessment_year": 2023,
    "pillars": [
        {
        "name": "EP",
        "areas": [
            {
            "name": "EP.1",
            "assessment": "Partial",
            "indicators": [
                {
                "name": "EP.1.a",
                "assessment": "Yes",
                "metrics": [
                    {
                    "name": "EP.1.a.i",
                    "value": "",
                    "source": {
                        "source_name": ""
                    }
                    },
                    {
                    "name": "EP.1.a.ii",
                    "value": "",
                    "source": {
                        "source_name": ""
                    }
                    }
                ],
                "source": {
                    "source_name": ""
                }
                },
                {
                "name": "EP.1.b",
                "assessment": "No",
                "metrics": [],
                "source": {
                    "source_name": "https://1p5ndc-pathways.climateanalytics.org/"
                }
                },
                {
                "name": "EP.1.c",
                "assessment": "No",
                "metrics": [],
                "source": {
                    "source_name": "https://transitionpathwayinitiative.org/publications/uploads/2023-ascor-framework-methodology-note"
                }
                }
            ]
            },
            {
            "name": "EP.2",
            "assessment": "Partial",
            "indicators": [
                {
                "name": "EP.2.a",
                "assessment": "Yes",
                "metrics": [
                    {
                    "name": "EP.2.a.i",
                    "value": "2022",
                    "source": {
                        "source_name": "https://unfccc.int/sites/default/files/NDC/2022-06/Canada%27s%20Enhanced%20NDC%20Submission1_FINAL%20EN.pdf"
                    }
                    }
                ],
                "source": {
                    "source_name": "https://unfccc.int/sites/default/files/NDC/2022-06/Canada%27s%20Enhanced%20NDC%20Submission1_FINAL%20EN.pdf"
                }
                },
                {
                "name": "EP.2.b",
                "assessment": "No",
                "metrics": [
                    {
                    "name": "EP.2.b.i",
                    "value": "",
                    "source": {
                        "source_name": ""
                    }
                    }
                ],
                "source": {
                    "source_name": "https://unfccc.int/sites/default/files/NDC/2022-06/Canada%27s%20Enhanced%20NDC%20Submission1_FINAL%20EN.pdf"
                }
                },
                {
                "name": "EP.2.c",
                "assessment": "No",
                "metrics": [
                    {
                    "name": "EP.2.c.i",
                    "value": "2021.0",
                    "source": {
                        "source_name": "https://1p5ndc-pathways.climateanalytics.org/"
                    }
                    }
                ],
                "source": {
                    "source_name": "https://1p5ndc-pathways.climateanalytics.org/"
                }
                },
                {
                "name": "EP.2.d",
                "assessment": "No",
                "metrics": [
                    {
                    "name": "EP.2.d.i",
                    "value": "2023.0",
                    "source": {
                        "source_name": "https://transitionpathwayinitiative.org/publications/uploads/2023-ascor-framework-methodology-note"
                    }
                    }
                ],
                "source": {
                    "source_name": "https://transitionpathwayinitiative.org/publications/uploads/2023-ascor-framework-methodology-note"
                }
                }
            ]
            },
            {
            "name": "EP.3",
            "assessment": "Partial",
            "indicators": [
                {
                "name": "EP.3.a",
                "assessment": "Yes",
                "metrics": [
                    {
                    "name": "EP.3.a.i",
                    "value": "2021.0",
                    "source": {
                        "source_name": "https://parl.ca/DocumentViewer/en/43-2/bill/C-12/royal-assent"
                    }
                    }
                ],
                "source": {
                    "source_name": "https://parl.ca/DocumentViewer/en/43-2/bill/C-12/royal-assent"
                }
                },
                {
                "name": "EP.3.b",
                "assessment": "Yes",
                "metrics": [],
                "source": {
                    "source_name": "https://parl.ca/DocumentViewer/en/43-2/bill/C-12/royal-assent"
                }
                },
                {
                "name": "EP.3.c",
                "assessment": "No",
                "metrics": [],
                "source": {
                    "source_name": "https://parl.ca/DocumentViewer/en/43-2/bill/C-12/royal-assent"
                }
                }
            ]
            }
        ]
        },
        {
        "name": "CP",
        "areas": [
            {
            "name": "CP.1",
            "assessment": "Yes",
            "indicators": [
                {
                "name": "CP.1.a",
                "assessment": "Yes",
                "metrics": [],
                "source": {
                    "source_name": "https://laws-lois.justice.gc.ca/eng/acts/C-19.3/FullText.html"
                }
                },
                {
                "name": "CP.1.b",
                "assessment": "Yes",
                "metrics": [],
                "source": {
                    "source_name": "https://laws-lois.justice.gc.ca/eng/acts/C-19.3/FullText.html"
                }
                }
            ]
            },
            {
            "name": "CP.2",
            "assessment": "Partial",
            "indicators": [
                {
                "name": "CP.2.a",
                "assessment": "Yes",
                "metrics": [],
                "source": {
                    "source_name": "https://laws-lois.justice.gc.ca/PDF/G-11.55.pdf"
                }
                },
                {
                "name": "CP.2.b",
                "assessment": "Yes",
                "metrics": [
                    {
                    "name": "CP.2.b.i",
                    "value": "2021.0",
                    "source": {
                        "source_name": "https://stats.oecd.org/Index.aspx?DataSetCode=ECR"
                    }
                    }
                ],
                "source": {
                    "source_name": "https://stats.oecd.org/Index.aspx?DataSetCode=ECR"
                }
                },
                {
                "name": "CP.2.c",
                "assessment": "No",
                "metrics": [
                    {
                    "name": "CP.2.c.i",
                    "value": "2023.0",
                    "source": {
                        "source_name": "https://laws-lois.justice.gc.ca/PDF/G-11.55.pdf"
                    }
                    }
                ],
                "source": {
                    "source_name": "https://www.carbonpricingleadership.org/leadershipreports"
                }
                }
            ]
            },
            {
            "name": "CP.3",
            "assessment": "Partial",
            "indicators": [
                {
                "name": "CP.3.a",
                "assessment": "Yes",
                "metrics": [
                    {
                    "name": "CP.3.a.i",
                    "value": "2021.0",
                    "source": {
                        "source_name": "https://pm.gc.ca/en/mandate-letters/2021/12/16/minister-environment-and-climate-change-mandate-letter"
                    }
                    }
                ],
                "source": {
                    "source_name": "https://www.canada.ca/content/dam/eccc/documents/pdf/climate-change/climate-plan/23043.01-%20Inefficient%20Fossil%20Fuel%20Subsidies%20Government%20of%20Canada%20Self%20Review-Framework_V02-EN.pdf"
                }
                },
                {
                "name": "CP.3.b",
                "assessment": "No",
                "metrics": [
                    {
                    "name": "CP.3.b.i",
                    "value": "2022.0",
                    "source": {
                        "source_name": "https://www.imf.org/en/Topics/climate-change/energy-subsidies"
                    }
                    }
                ],
                "source": {
                    "source_name": ""
                }
                },
                {
                "name": "CP.3.c",
                "assessment": "Yes",
                "metrics": [
                    {
                    "name": "CP.3.c.i",
                    "value": "2021.0",
                    "source": {
                        "source_name": "https://data.worldbank.org/indicator/NY.GDP.COAL.RT.ZS"
                    }
                    }
                ],
                "source": {
                    "source_name": "https://www.canada.ca/en/environment-climate-change/services/managing-pollution/energy-production/electricity-generation/statement-government-canada-thermal-coal-mining.html"
                }
                },
                {
                "name": "CP.3.d",
                "assessment": "No",
                "metrics": [
                    {
                    "name": "CP.3.d.i",
                    "value": "2021.0",
                    "source": {
                        "source_name": "https://data.worldbank.org/indicator/NY.GDP.PETR.RT.ZS"
                    }
                    },
                    {
                    "name": "CP.3.d.ii",
                    "value": "2021.0",
                    "source": {
                        "source_name": "https://data.worldbank.org/indicator/NY.GDP.NGAS.RT.ZS"
                    }
                    }
                ],
                "source": {
                    "source_name": ""
                }
                }
            ]
            },
            {
            "name": "CP.4",
            "assessment": "Partial",
            "indicators": [
                {
                "name": "CP.4.a",
                "assessment": "Yes",
                "metrics": [],
                "source": {
                    "source_name": "https://www.canada.ca/en/services/environment/weather/climatechange/climate-plan/climate-plan-overview/emissions-reduction-2030/plan.html"
                }
                },
                {
                "name": "CP.4.b",
                "assessment": "No",
                "metrics": [
                    {
                    "name": "CP.4.b.i",
                    "value": "2021.0",
                    "source": {
                        "source_name": "https://data.worldbank.org/indicator/EG.EGY.PRIM.PP.KD"
                    }
                    }
                ],
                "source": {
                    "source_name": ""
                }
                },
                {
                "name": "CP.4.c",
                "assessment": "Yes",
                "metrics": [],
                "source": {
                    "source_name": "https://www.budget.canada.ca/2022/pdf/budget-2022-en.pdf"
                }
                },
                {
                "name": "CP.4.d",
                "assessment": "Yes",
                "metrics": [
                    {
                    "name": "CP.4.d.i",
                    "value": "2021.0",
                    "source": {
                        "source_name": "https://www.iea.org/data-and-statistics/data-tools/energy-statistics-data-browser?country=WORLD&fuel=Energy%20supply&indicator=ElecGenByFuel"
                    }
                    }
                ],
                "source": {
                    "source_name": "https://www.canada.ca/en/services/environment/weather/climatechange/climate-plan/climate-plan-overview/emissions-reduction-2030/plan.html"
                }
                },
                {
                "name": "CP.4.e",
                "assessment": "Yes",
                "metrics": [
                    {
                    "name": "CP.4.e.i",
                    "value": "2022.0",
                    "source": {
                        "source_name": "https://www.ibat-alliance.org/country_profiles?locale=en"
                    }
                    }
                ],
                "source": {
                    "source_name": "https://data.worldbank.org/indicator/ER.LND.PTLD.ZS"
                }
                }
            ]
            },
            {
            "name": "CP.5",
            "assessment": "Partial",
            "indicators": [
                {
                "name": "CP.5.a",
                "assessment": "Yes",
                "metrics": [],
                "source": {
                    "source_name": "https://publications.gc.ca/collections/collection_2023/eccc/en4/En4-544-2023-eng.pdf"
                }
                },
                {
                "name": "CP.5.b",
                "assessment": "Yes",
                "metrics": [],
                "source": {
                    "source_name": "https://changingclimate.ca/site/assets/uploads/sites/3/2021/05/National-Issues-Report_Final_EN.pdf"
                }
                },
                {
                "name": "CP.5.c",
                "assessment": "No",
                "metrics": [],
                "source": {
                    "source_name": ""
                }
                },
                {
                "name": "CP.5.d",
                "assessment": "Yes",
                "metrics": [],
                "source": {
                    "source_name": "https://www.publicsafety.gc.ca/cnt/rsrcs/pblctns/mrgncy-mngmnt-strtgy/index-en.aspx"
                }
                },
                {
                "name": "CP.5.e",
                "assessment": "Exempt",
                "metrics": [],
                "source": {
                    "source_name": ""
                }
                }
            ]
            },
            {
            "name": "CP.6",
            "assessment": "Partial",
            "indicators": [
                {
                "name": "CP.6.a",
                "assessment": "No",
                "metrics": [
                    {
                    "name": "CP.6.a.i",
                    "value": "2021",
                    "source": {
                        "source_name": "https://data.worldbank.org/indicator/VA.PER.RNK"
                    }
                    }
                ],
                "source": {
                    "source_name": "https://www.ilo.org/dyn/normlex/en/f?p=1000:11300:0::NO:11300:P11300_INSTRUMENT_ID:312314"
                }
                },
                {
                "name": "CP.6.b",
                "assessment": "Yes",
                "metrics": [],
                "source": {
                    "source_name": "https://www.canada.ca/en/services/jobs/training/initiatives/sustainable-jobs/plan.html"
                }
                },
                {
                "name": "CP.6.c",
                "assessment": "Yes",
                "metrics": [],
                "source": {
                    "source_name": "https://www.canada.ca/en/services/jobs/training/initiatives/sustainable-jobs/plan.html"
                }
                },
                {
                "name": "CP.6.d",
                "assessment": "Yes",
                "metrics": [],
                "source": {
                    "source_name": "https://laws-lois.justice.gc.ca/PDF/G-11.55.pdf"
                }
                }
            ]
            }
        ]
        },
        {
        "name": "CF",
        "areas": [
            {
            "name": "CF.1",
            "assessment": "No",
            "indicators": [
                {
                "name": "CF.1.a",
                "assessment": "No",
                "metrics": [
                    {
                    "name": "CF.1.a.i",
                    "value": "2020.0",
                    "source": {
                        "source_name": "https://unfccc.int/BR5"
                    }
                    }
                ],
                "source": {
                    "source_name": "https://unfccc.int/BR5"
                }
                },
                {
                "name": "CF.1.b",
                "assessment": "No",
                "metrics": [
                    {
                    "name": "CF.1.b.i",
                    "value": "2021.0",
                    "source": {
                        "source_name": "https://webarchive.nationalarchives.gov.uk/ukgwa/20230401054904/https:/ukcop26.org/wp-content/uploads/2021/11/Table-of-climate-finance-commitments-November-2021.pdf"
                    }
                    }
                ],
                "source": {
                    "source_name": "https://webarchive.nationalarchives.gov.uk/ukgwa/20230401054904/https:/ukcop26.org/wp-content/uploads/2021/11/Table-of-climate-finance-commitments-November-2021.pdf"
                }
                }
            ]
            },
            {
            "name": "CF.2",
            "assessment": "Exempt",
            "indicators": [
                {
                "name": "CF.2.a",
                "assessment": "Exempt",
                "metrics": [],
                "source": {
                    "source_name": ""
                }
                },
                {
                "name": "CF.2.b",
                "assessment": "Exempt",
                "metrics": [],
                "source": {
                    "source_name": ""
                }
                }
            ]
            },
            {
            "name": "CF.3",
            "assessment": "Yes",
            "indicators": [
                {
                "name": "CF.3.a",
                "assessment": "Yes",
                "metrics": [],
                "source": {
                    "source_name": "https://www.budget.canada.ca/2023/pdf/budget-gdql-egdqv-2023-en.pdf"
                }
                },
                {
                "name": "CF.3.b",
                "assessment": "Yes",
                "metrics": [],
                "source": {
                    "source_name": "https://www.budget.canada.ca/2023/pdf/budget-gdql-egdqv-2023-en.pdf"
                }
                }
            ]
            },
            {
            "name": "CF.4",
            "assessment": "Not applicable",
            "indicators": []
            }
        ]
        }
    ]
    }

# --------------------------------------------------------------------------
# Company endpoint fixtures
# --------------------------------------------------------------------------
@pytest.fixture
def expected_all_companies_response():
    """Expected response structure for get all companies endpoints with page 1 and 10 results per page"""
    return {
    "total": 2060,
    "page": 1,
    "per_page": 10,
    "companies": [
        {
        "company_id": "yankuang_energy",
        "name": "yankuang energy",
        "sector": "Coal Mining",
        "geography": "China",
        "latest_assessment_year": None
        },
        {
        "company_id": "3m",
        "name": "3m",
        "sector": "Industrials",
        "geography": "United States of America",
        "latest_assessment_year": None
        },
        {
        "company_id": "a2a",
        "name": "a2a",
        "sector": "Electricity Utilities",
        "geography": "Italy",
        "latest_assessment_year": None
        },
        {
        "company_id": "abb",
        "name": "abb",
        "sector": "Industrials",
        "geography": "Switzerland",
        "latest_assessment_year": None
        },
        {
        "company_id": "acc",
        "name": "acc",
        "sector": "Cement",
        "geography": "India",
        "latest_assessment_year": None
        },
        {
        "company_id": "acs_group",
        "name": "acs group",
        "sector": "Industrials",
        "geography": "Spain",
        "latest_assessment_year": None
        },
        {
        "company_id": "acwa_power",
        "name": "acwa power",
        "sector": "Electricity Utilities",
        "geography": "Saudi Arabia",
        "latest_assessment_year": None
        },
        {
        "company_id": "adama",
        "name": "adama",
        "sector": "Chemicals",
        "geography": "China",
        "latest_assessment_year": None
        },
        {
        "company_id": "adbri",
        "name": "adbri",
        "sector": "Cement",
        "geography": "Australia",
        "latest_assessment_year": None
        },
        {
        "company_id": "adnoc_drilling_company",
        "name": "adnoc drilling company",
        "sector": "Oil & Gas",
        "geography": "United Arab Emirates",
        "latest_assessment_year": None
        }
    ]
    }

@pytest.fixture
def expected_company_details_response():
    """Expected response structure for get company details endpoints with 3m as example"""
    return {
  "company_id": "3m",
  "name": "3m",
  "sector": "Industrials",
  "geography": "United States of America",
  "latest_assessment_year": None,
  "management_quality_score": 3,
  "carbon_performance_alignment_2035": "N/A",
  "emissions_trend": "down"
}

@pytest.fixture
def expected_company_history_response():
    """Expected response structure for get company history endpoints with 3m as example"""
    return {
  "company_id": "3m",
  "history": [
    {
      "company_id": "3m",
      "name": "3m",
      "sector": "Industrials",
      "geography": "United States of America",
      "latest_assessment_year": 2024,
      "management_quality_score": 3,
      "carbon_performance_alignment_2035": "nan",
      "emissions_trend": "down"
    }
  ]
}

@pytest.fixture
def expected_company_performance_comparison_response():
    """Expected response structure for get company history endpoints with 3m as example"""
    return {
  "company_id": "3m",
  "message": "Only one record exists for '3m', so performance comparison is not possible.",
  "available_assessment_years": [
    2024
  ]
}

# --------------------------------------------------------------------------
# MQ endpoint fixtures
# --------------------------------------------------------------------------

@pytest.fixture
def expected_latest_mq_assessment_reponse():
    """Expected response structure for latest management quality endpoint using page 1, 10 results per page as example"""
    return {
  "total_records": 2060,
  "page": 1,
  "page_size": 10,
  "results": [
    {
      "company_id": "Yunnan Tin",
      "name": "Yunnan Tin",
      "sector": "Basic Materials",
      "geography": "China",
      "latest_assessment_year": 2024,
      "management_quality_score": None
    },
    {
      "company_id": "Loln Electric Holdings",
      "name": "Loln Electric Holdings",
      "sector": "Industrials",
      "geography": "United States of America",
      "latest_assessment_year": 2024,
      "management_quality_score": None
    },
    {
      "company_id": "Beacon Roofing Supply",
      "name": "Beacon Roofing Supply",
      "sector": "Industrials",
      "geography": "United States of America",
      "latest_assessment_year": 2024,
      "management_quality_score": None
    },
    {
      "company_id": "SDIC Power Holdings",
      "name": "SDIC Power Holdings",
      "sector": "Electricity Utilities",
      "geography": "China",
      "latest_assessment_year": 2024,
      "management_quality_score": None
    },
    {
      "company_id": "HBIS",
      "name": "HBIS",
      "sector": "Steel",
      "geography": "China",
      "latest_assessment_year": 2024,
      "management_quality_score": None
    },
    {
      "company_id": "Hengtong Optic-Electric",
      "name": "Hengtong Optic-Electric",
      "sector": "Technology",
      "geography": "China",
      "latest_assessment_year": 2024,
      "management_quality_score": None
    },
    {
      "company_id": "Wens Foodstuff Group",
      "name": "Wens Foodstuff Group",
      "sector": "Food Producers",
      "geography": "China",
      "latest_assessment_year": 2024,
      "management_quality_score": None
    },
    {
      "company_id": "Shanghai Jin Jiang International Hotels",
      "name": "Shanghai Jin Jiang International Hotels",
      "sector": "Consumer Services",
      "geography": "China",
      "latest_assessment_year": 2024,
      "management_quality_score": None
    },
    {
      "company_id": "Shenzhen Energy Group",
      "name": "Shenzhen Energy Group",
      "sector": "Electricity Utilities",
      "geography": "China",
      "latest_assessment_year": 2024,
      "management_quality_score": None
    },
    {
      "company_id": "Yunnan Chihong Z & Germanium",
      "name": "Yunnan Chihong Z & Germanium",
      "sector": "Basic Materials",
      "geography": "China",
      "latest_assessment_year": 2024,
      "management_quality_score": None
    }
  ]
}

@pytest.fixture
def expected_latest_mq_methodology_reponse():
    """Expected response structure for MQ methodology endpoint using MQ 1, page 1, and 10 results per page as example"""
    return {
  "total_records": 140,
  "page": 1,
  "page_size": 10,
  "results": [
    {
      "company_id": " Yankuang Energy",
      "name": " Yankuang Energy",
      "sector": "Coal Mining",
      "geography": "China",
      "latest_assessment_year": 2017,
      "management_quality_score": None
    },
    {
      "company_id": "ADBRI",
      "name": "ADBRI",
      "sector": "Cement",
      "geography": "Australia",
      "latest_assessment_year": 2016,
      "management_quality_score": None
    },
    {
      "company_id": "APA Corporation",
      "name": "APA Corporation",
      "sector": "Oil & Gas",
      "geography": "United States of America",
      "latest_assessment_year": 2015,
      "management_quality_score": None
    },
    {
      "company_id": "Acerinox",
      "name": "Acerinox",
      "sector": "Steel",
      "geography": "Spain",
      "latest_assessment_year": 2016,
      "management_quality_score": None
    },
    {
      "company_id": "Adaro Energy",
      "name": "Adaro Energy",
      "sector": "Coal Mining",
      "geography": "Indonesia",
      "latest_assessment_year": 2017,
      "management_quality_score": None
    },
    {
      "company_id": "African Rainbow Minerals",
      "name": "African Rainbow Minerals",
      "sector": "Coal Mining",
      "geography": "South Africa",
      "latest_assessment_year": 2017,
      "management_quality_score": None
    },
    {
      "company_id": "Ambuja Cements",
      "name": "Ambuja Cements",
      "sector": "Cement",
      "geography": "India",
      "latest_assessment_year": 2016,
      "management_quality_score": None
    },
    {
      "company_id": "American Electric Power",
      "name": "American Electric Power",
      "sector": "Electricity Utilities",
      "geography": "United States of America",
      "latest_assessment_year": 2016,
      "management_quality_score": None
    },
    {
      "company_id": "Anadarko Petroleum",
      "name": "Anadarko Petroleum",
      "sector": "Oil & Gas",
      "geography": "United States of America",
      "latest_assessment_year": 2015,
      "management_quality_score": None
    },
    {
      "company_id": "Anglo American (Coal Mining)",
      "name": "Anglo American (Coal Mining)",
      "sector": "Coal Mining",
      "geography": "United Kingdom",
      "latest_assessment_year": 2016,
      "management_quality_score": None
    }
  ]
}

@pytest.fixture
def expected_mq_sector_trends_reponse():
    """Expected response structure for latest management quality endpoint using "coal mining", page 1, and 10 results per page as example"""
    return {
  "total_records": 381,
  "page": 1,
  "page_size": 10,
  "results": [
    {
      "company_id": "Teck Resources (Coal Mining)",
      "name": "Teck Resources (Coal Mining)",
      "sector": "coal mining",
      "geography": "Canada",
      "latest_assessment_year": 2019,
      "management_quality_score": None
    },
    {
      "company_id": "African Rainbow Minerals",
      "name": "African Rainbow Minerals",
      "sector": "coal mining",
      "geography": "South Africa",
      "latest_assessment_year": 2018,
      "management_quality_score": None
    },
    {
      "company_id": "Whitehaven Coal",
      "name": "Whitehaven Coal",
      "sector": "coal mining",
      "geography": "Australia",
      "latest_assessment_year": 2023,
      "management_quality_score": None
    },
    {
      "company_id": "Whitehaven Coal",
      "name": "Whitehaven Coal",
      "sector": "coal mining",
      "geography": "Australia",
      "latest_assessment_year": 2023,
      "management_quality_score": None
    },
    {
      "company_id": "Whitehaven Coal",
      "name": "Whitehaven Coal",
      "sector": "coal mining",
      "geography": "Australia",
      "latest_assessment_year": 2021,
      "management_quality_score": None
    },
    {
      "company_id": "Bumi",
      "name": "Bumi",
      "sector": "coal mining",
      "geography": "Indonesia",
      "latest_assessment_year": 2021,
      "management_quality_score": None
    },
    {
      "company_id": "ENN Ecological Holdings",
      "name": "ENN Ecological Holdings",
      "sector": "coal mining",
      "geography": "China",
      "latest_assessment_year": 2021,
      "management_quality_score": None
    },
    {
      "company_id": "DMCI",
      "name": "DMCI",
      "sector": "coal mining",
      "geography": "Philippines",
      "latest_assessment_year": 2021,
      "management_quality_score": None
    },
    {
      "company_id": "Coronado Global Resources",
      "name": "Coronado Global Resources",
      "sector": "coal mining",
      "geography": "Australia",
      "latest_assessment_year": 2021,
      "management_quality_score": None
    },
    {
      "company_id": "Consol Energy",
      "name": "Consol Energy",
      "sector": "coal mining",
      "geography": "United States of America",
      "latest_assessment_year": 2021,
      "management_quality_score": None
    }
  ]
    }

# --------------------------------------------------------------------------
# CP endpoint fixtures
# --------------------------------------------------------------------------
@pytest.fixture
def expected_latest_cp_reponse():
    """Expected response structure for latest CP assessment endpoint using page 1 and 10 results per page as example"""
    return [
        {
            "company_id": "Vectren",
            "name": "Vectren",
            "sector": "Electricity Utilities",
            "geography": "United States of America",
            "latest_assessment_year": 2019,
            "carbon_performance_2025": "Not Aligned",
            "carbon_performance_2027": "Not Aligned",
            "carbon_performance_2035": "Not Aligned",
            "carbon_performance_2050": "Not Aligned"
        },
        {
            "company_id": "Innogy",
            "name": "Innogy",
            "sector": "Electricity Utilities",
            "geography": "Germany",
            "latest_assessment_year": 2019,
            "carbon_performance_2025": "Not Aligned",
            "carbon_performance_2027": "Not Aligned",
            "carbon_performance_2035": "Not Aligned",
            "carbon_performance_2050": "Below 2 Degrees"
        },
        {
            "company_id": "Anadarko Petroleum",
            "name": "Anadarko Petroleum",
            "sector": "Oil & Gas",
            "geography": "United States of America",
            "latest_assessment_year": 2019,
            "carbon_performance_2025": "Not Aligned",
            "carbon_performance_2027": "Not Aligned",
            "carbon_performance_2035": "Not Aligned",
            "carbon_performance_2050": "Not Aligned"
        },
        {
            "company_id": "Inner Mongolia Yili Industrial",
            "name": "Inner Mongolia Yili Industrial",
            "sector": "Food Producers",
            "geography": "China",
            "latest_assessment_year": 2024,
            "carbon_performance_2025": "Not Aligned",
            "carbon_performance_2027": "Not Aligned",
            "carbon_performance_2035": "Not Aligned",
            "carbon_performance_2050": "Not Aligned"
        },
        {
            "company_id": "Orkla",
            "name": "Orkla",
            "sector": "Food Producers",
            "geography": "Norway",
            "latest_assessment_year": 2024,
            "carbon_performance_2025": "Not Aligned",
            "carbon_performance_2027": "Not Aligned",
            "carbon_performance_2035": "Not Aligned",
            "carbon_performance_2050": "Not Aligned"
        },
        {
            "company_id": "Freshpet",
            "name": "Freshpet",
            "sector": "Food Producers",
            "geography": "United States of America",
            "latest_assessment_year": 2024,
            "carbon_performance_2025": "Not Aligned",
            "carbon_performance_2027": "Not Aligned",
            "carbon_performance_2035": "Not Aligned",
            "carbon_performance_2050": "Not Aligned"
        },
        {
            "company_id": "NH Foods",
            "name": "NH Foods",
            "sector": "Food Producers",
            "geography": "Japan",
            "latest_assessment_year": 2024,
            "carbon_performance_2025": "Not Aligned",
            "carbon_performance_2027": "Not Aligned",
            "carbon_performance_2035": "Not Aligned",
            "carbon_performance_2050": "Not Aligned"
        },
        {
            "company_id": "Ingredion",
            "name": "Ingredion",
            "sector": "Food Producers",
            "geography": "United States of America",
            "latest_assessment_year": 2024,
            "carbon_performance_2025": "Not Aligned",
            "carbon_performance_2027": "Not Aligned",
            "carbon_performance_2035": "Not Aligned",
            "carbon_performance_2050": "Not Aligned"
        },
        {
            "company_id": "Yakult Honsha",
            "name": "Yakult Honsha",
            "sector": "Food Producers",
            "geography": "Japan",
            "latest_assessment_year": 2024,
            "carbon_performance_2025": "Not Aligned",
            "carbon_performance_2027": "Not Aligned",
            "carbon_performance_2035": "Not Aligned",
            "carbon_performance_2050": "Not Aligned"
        },
        {
            "company_id": "Foshan Haitian Flavouring and Food",
            "name": "Foshan Haitian Flavouring and Food",
            "sector": "Food Producers",
            "geography": "China",
            "latest_assessment_year": 2024,
            "carbon_performance_2025": "Not Aligned",
            "carbon_performance_2027": "Not Aligned",
            "carbon_performance_2035": "Not Aligned",
            "carbon_performance_2050": "Not Aligned"
        }
    ]

@pytest.fixture
def expected_company_cp_history_reponse():
    """Expected response structure for latest CP assessment histroy endpoint using AES as example"""
    return [
        {
            "company_id": "AES",
            "name": "AES",
            "sector": "Electricity Utilities",
            "geography": "United States of America",
            "latest_assessment_year": 2024,
            "carbon_performance_2025": "Not Aligned",
            "carbon_performance_2027": "Not Aligned",
            "carbon_performance_2035": "Not Aligned",
            "carbon_performance_2050": "Not Aligned"
        },
        {
            "company_id": "AES",
            "name": "AES",
            "sector": "Electricity Utilities",
            "geography": "United States of America",
            "latest_assessment_year": 2023,
            "carbon_performance_2025": "Not Aligned",
            "carbon_performance_2027": "Not Aligned",
            "carbon_performance_2035": "Not Aligned",
            "carbon_performance_2050": "Not Aligned"
        },
        {
            "company_id": "AES",
            "name": "AES",
            "sector": "Electricity Utilities",
            "geography": "United States of America",
            "latest_assessment_year": 2022,
            "carbon_performance_2025": "Not Aligned",
            "carbon_performance_2027": "Not Aligned",
            "carbon_performance_2035": "Not Aligned",
            "carbon_performance_2050": "Not Aligned"
        },
        {
            "company_id": "AES",
            "name": "AES",
            "sector": "Electricity Utilities",
            "geography": "United States of America",
            "latest_assessment_year": 2021,
            "carbon_performance_2025": "Not Aligned",
            "carbon_performance_2027": "Not Aligned",
            "carbon_performance_2035": "Not Aligned",
            "carbon_performance_2050": "Not Aligned"
        },
        {
            "company_id": "AES",
            "name": "AES",
            "sector": "Electricity Utilities",
            "geography": "United States of America",
            "latest_assessment_year": 2020,
            "carbon_performance_2025": "Not Aligned",
            "carbon_performance_2027": "Not Aligned",
            "carbon_performance_2035": "Not Aligned",
            "carbon_performance_2050": "Not Aligned"
        },
        {
            "company_id": "AES",
            "name": "AES",
            "sector": "Electricity Utilities",
            "geography": "United States of America",
            "latest_assessment_year": 2019,
            "carbon_performance_2025": "Not Aligned",
            "carbon_performance_2027": "Not Aligned",
            "carbon_performance_2035": "Not Aligned",
            "carbon_performance_2050": "Not Aligned"
        }
    ]

@pytest.fixture
def expected_cp_alignment_reponse():
    """Expected response structure for latest CP alignment endpoint using AES as example"""
    return {
  "2025": "Not Aligned",
  "2027": "Not Aligned",
  "2035": "Not Aligned",
  "2050": "Not Aligned"
    }

@pytest.fixture
def expected_cp_comparison_reponse():
    """Expected response structure for endpoint comparing the most recent CP assessment to the previous one, using AES as example"""
    return {
        "company_id": "AES",
        "current_year": 2022,
        "previous_year": 2020,
        "latest_cp_2025": "Not Aligned",
        "previous_cp_2025": "Not Aligned",
        "latest_cp_2035": "Not Aligned",
        "previous_cp_2035": "Not Aligned"
    }

# ------------------------------------------------------------------------------
# Home endpoint fixtures
# ------------------------------------------------------------------------------
@pytest.fixture
def expected_home_response():
    """Expected response structure for API home endpoint"""
    return {
        "message": "Welcome to the TPI API!"
    }   