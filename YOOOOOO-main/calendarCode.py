import calendar
import pandas as pd

def generate_calendar(selected_year, selected_month, events):
    cal = calendar.monthcalendar(selected_year, selected_month)
    df = pd.DataFrame(cal, columns=["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])
    for week in df.index:
        for day in df.columns:
            if df.loc[week, day] != 0:
                date_str = f"{selected_year}-{selected_month:02d}-{df.loc[week, day]:02d}"
                if date_str in events:
                    df.loc[week, day] = f"{df.loc[week, day]}\n"
    return df