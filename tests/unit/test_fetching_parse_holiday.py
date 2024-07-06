import pytest
from Holiday_Detection_Parsing.extracting_parsing_holidays import parse_holidays

@pytest.fixture
def sample_data():
    return '''<div class="field field-name-body">
         <table>
            <thead>
               <tr>
                  <th scope="row">&nbsp;</th>
                  <th scope="col">2024</th>
                  <th scope="col">2025</th>
                  <th scope="col">2026</th>
               </tr>
            </thead>
            <tbody>
               <tr>
                  <th scope="row"><strong>New Year's Day</strong></th>
                  <td>Monday 1 January</td>
                  <td>Wednesday 1 January</td>
                  <td>Thursday 1 January</td>
               </tr>
               <tr>
                  <th scope="row"><strong>Australia Day</strong></th>
                  <td>Friday 26 January</td>
                  <td>Monday 27 January</td>
                  <td>Monday 26 January</td>
               </tr>
               <tr>
                  <th scope="row"><strong>Labour Day</strong></th>
                  <td>Monday 4 March</td>
                  <td>Monday 3 March</td>
                  <td>Monday 2 March</td>
               </tr>
               <tr>
                  <th scope="row"><strong>Good Friday</strong></th>
                  <td>Friday 29 March</td>
                  <td>Friday 18 April</td>
                  <td>Friday 3 April</td>
               </tr>
            </tbody>
         </table>
    </div>'''

def test_parse_holiday(sample_data):
    actual_output = parse_holidays(sample_data)
    print(actual_output)
    expected_output = [{'Year': 2024, 'Holiday Date': "Monday 1 January",'Holiday Name': "New Year's Day"},
                       {'Year': 2025, 'Holiday Date': "Wednesday 1 January", 'Holiday Name': "New Year's Day"},
                       {'Year': 2024, 'Holiday Date': "Friday 26 January", 'Holiday Name': "Australia Day"},
                       {'Year': 2025, 'Holiday Date': "Monday 27 January", 'Holiday Name': "Australia Day"},
                       {'Year': 2024, 'Holiday Date': "Monday 4 March", 'Holiday Name': "Labour Day"},
                       {'Year': 2025, 'Holiday Date': "Monday 3 March", 'Holiday Name': "Labour Day"},
                       {'Year': 2024, 'Holiday Date': "Friday 29 March", 'Holiday Name': "Good Friday"},
                       {'Year': 2025, 'Holiday Date': "Friday 18 April", 'Holiday Name': "Good Friday"}]
    assert actual_output == expected_output

def test_parse_holiday_empty_input():
    sample_data = ''
    actual_output = parse_holidays(sample_data)
    assert actual_output == []

def test_parse_holiday_blank_element():
    sample_data = '<html><body><table></table></body></html>'
    actual_output = parse_holidays(sample_data)
    assert actual_output == []

