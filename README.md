# **Belief Distribution Elicitation App**

This oTree application implements a belief distribution elicitation method introduced in the paper:

**Direct Elicitation of Parametric Belief Distributions: An Application to Inflation Expectations**  
**Authors:** Pedro Gonzalez-Fernandez, Ciril Bosch-Rosa, Thomas Meissner  

---

## **Overview**

This application allows researchers to directly elicit participants' beliefs about future inflation rates using parametric distributions. Participants provide their minimum and maximum plausible inflation rates and adjust sliders to specify the mean and variance of their expected inflation distribution.

---

## **Citation Requirement**

If you use this application for your research, please cite the following paper:

**Gonzalez-Fernandez, P., Bosch-Rosa, C., & Meissner, T.**  
[Direct Elicitation of Parametric Belief Distributions: An Application to Inflation Expectations.](https://opus4.kobv.de/opus4-hsog/frontdoor/deliver/index/docId/5604/file/BSoE_DP_0048.pdf)

---

## **Requirements**

- **Python**: 3.11.5 or higher  
- **oTree**: 5.11.1 or higher  
- Additional dependencies as listed in `requirements.txt`  

---

## **Installation**

1. **Clone the repository:**

   ```bash
   git clone https://github.com/TGKMeissner/BetaBeliefs.git
   ```

2. **Navigate to the project directory:**

   ```bash
   cd BetaBeliefs
   ```

3. **Install required packages:**

   ```bash
   pip install -r requirements.txt
   ```

---

## **Running the App**

1. **Start the oTree development server:**

   ```bash
   otree devserver
   ```

2. **Access the app in your web browser:**

   ```
   http://localhost:8000
   ```

---

## **App Structure**

- **Core Files**:
  - `__init__.py`: Defines the app’s models and pages.
- **Templates**:
  - `MinMaxInput.html`: Collects minimum and maximum inflation rates.
  - `Sliders.html`: Includes sliders for mean and variance adjustments with an interactive plot.
  - `Results.html`: Displays a summary of participants' responses.

---

## **References**

For a detailed explanation of the methodology and application, refer to the original paper:

**Gonzalez-Fernandez, P., Bosch-Rosa, C., & Meissner, T.**  

[Direct Elicitation of Parametric Belief Distributions: An Application to Inflation Expectations.](https://opus4.kobv.de/opus4-hsog/frontdoor/deliver/index/docId/5604/file/BSoE_DP_0048.pdf)

---

## **Authors**

- **Pedro Gonzalez-Fernandez**  
- **Ciril Bosch-Rosa**  
- **Thomas Meissner**

---
