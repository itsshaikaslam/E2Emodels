import requests
from ipywidgets import Label, BoundedFloatText, BoundedIntText, Dropdown, Button, Output, VBox

prescribe_label = Label('Drug prescription prediction for age, gender, bp, cholesterol and "Na to K"')
age_text = BoundedIntText(min=16, max=100, value=47, description="Age:", disabled=False)
gender_dropdown = Dropdown(options=['F', 'M'], description='Gender:', disabled=False)
bp_dropdown = Dropdown(options=['HIGH', 'LOW', 'NORMAL'], value="LOW", description='BP:', disabled=False)
cholesterol_dropdown = Dropdown(options=['HIGH', 'NORMAL'], description='Cholesterol:', disabled=False)
na_to_k_text = BoundedFloatText(min=0.0, max=50.0, value=14, description="Na to K", disabled=False)
prescribe_button = Button(description="Presribe")
prescribe_output = Output()

# Button click event handlers ...
def prescribe_button_on_click(b):
    request_url = f"https://itsshaikaslamwebapp11.azurewebsites.net//drug?Age={age_text.value}&Sex={gender_dropdown.value}&BP={bp_dropdown.value}&Cholesterol={cholesterol_dropdown.value}&Na_to_K={na_to_k_text.value}"
    response = requests.get(request_url)
    recommended_drug = response.json()["recommended_drug"]

    prescribe_output.clear_output()
    with prescribe_output:

        print(f"The recommended drug is {recommended_drug}")
        
prescribe_button.on_click(prescribe_button_on_click)

vbox_prescribe = VBox([prescribe_label, age_text, gender_dropdown, bp_dropdown, cholesterol_dropdown, na_to_k_text, prescribe_button, prescribe_output])