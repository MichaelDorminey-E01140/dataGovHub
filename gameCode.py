import streamlit as st
import pandas as pd
import time
import random
from dataBase import * 

def startingGame():
    st.title("Data Cleaning Game")

    # Game button to start
    if st.button("Start Data Cleaning Game"):
        st.session_state.game_started = True
        st.session_state.start_time = time.time()

    # Start game logic
    if st.session_state.get("game_started", False):
        playerName = st.text_input("Enter your Name or Nickname:", "")
        if playerName:
            st.write(f"Welcome, {playerName}! You will be cleaning cafe sales data.")

            # Load dataset
            filePath = "cafeSales.csv"
            fullDF = pd.read_csv(filePath)
            subsetSize = 50
            df = fullDF.sample(n=subsetSize, random_state=random.randint(1, 1000)).sort_index()
            score = 100

            # Store data in session to prevent resets
            if "df" not in st.session_state:
                st.session_state.df = df.copy()
                st.session_state.missing_values = df.isnull().sum().sum()
                st.session_state.duplicate_rows = df.duplicated().sum()
                st.session_state.error_indices = []

            df = st.session_state.df  

            # Detect Errors
            actual_columns = df.columns.tolist()
            expected_columns = ["Item", "Quantity", "Price Per Unit", "Total Spent", "Payment Method", "Location", "Transaction Date"]
            error_columns = [col for col in expected_columns if col in actual_columns]

            def isInvalid(value, column):
                if pd.isnull(value):  
                    return False
                if column in expected_columns:
                    return str(value).lower() in [ "error", "invalid", ""]
                return False

            if error_columns:
                error_rows = df[error_columns].apply(lambda row: any(isInvalid(row[col], col) for col in error_columns), axis=1)
                st.session_state.error_indices = sorted(df[error_rows].index.tolist()) 

            # Display raw data (sorted)
            st.write("🔍 **Raw Data Sample (Sorted by Index):**")
            st.dataframe(df)

            # Display issues
            st.write("🚨 **Data Issues Detected:**")
            st.write(f"🔴 Missing Value Rows: {st.session_state.missing_values}")
            st.write(f"🔴 Duplicate Rows: {st.session_state.duplicate_rows}")
            st.write(f"🔴 Error Rows: {len(st.session_state.error_indices)}")

            # Fix missing values one by one (dropdown sorted)
            missing_rows = df[df.isnull().any(axis = 1)].index.tolist()
            st.session_state.missing_values = len(missing_rows)
            missing_index = sorted(df.index.tolist())
            selected_row = st.selectbox("Select row to fix missing values:",missing_index)
            if st.button("Fill Missing Values in Selected Row"):
                if selected_row in missing_rows:
                    df.loc[selected_row] = df.loc[selected_row].fillna("Unknown")
                    st.session_state.df = df  
                    st.session_state.missing_values = len(df[df.isnull().any(axis=1)])
                    st.success("Missing values in row {selected_row} fixed!")
                    st.rerun()
                else: 
                    st.write("Not a valid row with a missing value")
                    score -= 1 
                return score



            # Remove duplicates one by one 
            if "Transaction ID" in df.columns:
                st.session_state.duplicate_rows = df.duplicated(subset = ["Transaction ID"]).sum()
                duplicate_index = sorted(df.index.tolist())  
                selected_dup = st.selectbox("Select duplicate row to delete:", duplicate_index)
                if st.button("Delete Selected Duplicate Row"):
                    if selected_dup in df[df.duplicated()].index.tolist():
                        df.drop(index=selected_dup, inplace=True)
                        st.session_state.df = df  
                        st.session_state.duplicate_rows = df.duplicated().sum()
                        st.success(f"Duplicate row {selected_dup} removed!")
                        st.rerun() 
                    else:
                        st.write("Not a valid row with an duplicate please choose the second time the row repeats based on Transaction ID")
                        score -= 1 
                    return score

            # Remove error rows 
            if len(st.session_state.error_indices) > 0:
                error_index = sorted(df.index.tolist())
                selected_error = st.selectbox("Select error row to delete:", error_index)
                if st.button("Delete Selected Error Row"):
                    if selected_error in st.session_state.error_indices:
                        st.session_state.df = st.session_state.df.drop(index=selected_error)
                        st.session_state.error_indices.remove(selected_error)                        
                        st.success(f"Error row {selected_error} removed!")
                        st.rerun()
                    else:
                        st.write("Not a valid row with an error") 
                        score -= 1 
                return score

            # End Game
            if st.session_state.missing_values == 0 and st.session_state.duplicate_rows == 0 and len(st.session_state.error_indices) == 0:
                end_time = time.time()
                timeTaken = round(end_time - st.session_state.start_time, 2)
                timeTakenMinutes = round(timeTaken/60 , 2)
                score = score - (st.session_state.missing_values + st.session_state.duplicate_rows + len(st.session_state.error_indices))
                score = max(score, 0)

                st.write("🎉 **Game Completed!**")
                st.write(f"🏆 **Your Score: {score}**")
                st.write(f"⏳ **Time Taken: {timeTakenMinutes} minutes**")
                if st.checkbox("Submit Score to Leaderboard"):
                    updateGamePlayerData(playerName, score, timeTakenMinutes)
                    st.success("Your results have been successfully submitted to the leaderboard")
                
                    st.write("📊 **Leaderboard**")
                    gameLeaderboard = getGameLeaderboard()
                    if gameLeaderboard:
                        df = pd.DataFrame(gameLeaderboard, columns =  ["Player Name", "Score", "Time Taken (Minutes)"])
                        st.table(df)
               