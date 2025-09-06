# Module utils is only recognized as a package if i run this script in the root directory
import pandas as pd
from openliga.api_handler import get_available_sports

available_sports = get_available_sports()

sports_df = pd.DataFrame(available_sports)
print(sports_df)
