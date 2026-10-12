import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 1. Dashboard Header
st.set_page_config(layout="wide")
st.title("🌋 Live Tectonic & Earthquake Monitor")
st.markdown("This dashboard filters and visualises real-time seismic data syncing with NASA and the USGS.")

# 2. Sidebar Filters
st.sidebar.header("Filter Settings")
min_magnitude = st.sidebar.slider("Minimum Magnitude", 1.0, 10.0, 4.5)

# 3. Fetch Live Data
url = "https://usgs.gov"
df = pd.read_csv(url)

# 4. Filter Data based on slider choice
filtered_df = df[df['mag'] >= min_magnitude]

# 5. Create Layout Columns
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader(f"Global Map ({min_magnitude}+ Magnitude)")
    # Streamlit automatically turns latitude/longitude columns into a map
    st.map(filtered_df)

with col2:
    st.subheader("Depth vs Magnitude Analysis")
    # Build a scientific chart showing how deep the earthquakes are
    fig, ax = plt.subplots()
    ax.scatter(filtered_df['mag'], filtered_df['depth'], alpha=0.5, color='darkred')
    ax.set_xlabel("Magnitude")
    ax.set_ylabel("Depth (km)")
    ax.invert_yaxis()  # Invert so deeper events are at the bottom of the chart
    st.pyplot(fig)

# 6. Show Raw Data Table at the bottom
st.subheader("Recent Activity Data Log")
st.dataframe(filtered_df[['time', 'place', 'mag', 'depth', 'latitude', 'longitude']], use_container_width=True)
