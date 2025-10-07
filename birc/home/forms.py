from django import forms
from wagtail.admin.forms import WagtailAdminPageForm
import json


class SpeciesDataTableForm(WagtailAdminPageForm):
    columns_file = forms.FileField(
        required=False, 
        label="For Headers Label (must JSON File)",
        help_text="Upload JSON file containing an array of column names"
    )
    rows_file = forms.FileField(
        required=False,
        label="For Data Rows (must JSON File)", 
        help_text="Upload JSON file containing an array of row arrays"
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Add widget attrs for better UX
        self.fields['columns_file'].widget.attrs.update({
            'accept': '.json',
        })
        self.fields['rows_file'].widget.attrs.update({
            'accept': '.json',
        })

    def clean_columns_file(self):
        """Validate the columns JSON file."""
        columns_file = self.cleaned_data.get('columns_file')
        if columns_file:
            try:
                content = columns_file.read()
                columns_file.seek(0)
                
                columns_data = json.loads(content)
                if not isinstance(columns_data, list):
                    raise forms.ValidationError("Columns file must contain a JSON array.")
                if not all(isinstance(col, str) for col in columns_data):
                    raise forms.ValidationError("All column names must be strings.")
                return columns_file
            except json.JSONDecodeError as e:
                raise forms.ValidationError(f"Invalid JSON format: {str(e)}")
        return columns_file

    def clean_rows_file(self):
        """Validate the rows JSON file."""
        rows_file = self.cleaned_data.get('rows_file')
        if rows_file:
            try:
                content = rows_file.read()
                rows_file.seek(0)
                
                rows_data = json.loads(content)
                if not isinstance(rows_data, list):
                    raise forms.ValidationError("Rows file must contain a JSON array.")
                if not all(isinstance(row, list) for row in rows_data):
                    raise forms.ValidationError("Each row must be an array.")
                return rows_file
            except json.JSONDecodeError as e:
                raise forms.ValidationError(f"Invalid JSON format: {str(e)}")
        return rows_file

    def clean(self):
        """Validate that both files are provided together."""
        cleaned_data = super().clean()
        columns_file = cleaned_data.get('columns_file')
        rows_file = cleaned_data.get('rows_file')

        # If one file is provided, both should be provided
        if (columns_file and not rows_file) or (rows_file and not columns_file):
            raise forms.ValidationError(
                "Both columns and rows files must be uploaded together."
            )

        return cleaned_data