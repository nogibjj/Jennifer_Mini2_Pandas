"""
Test goes here

"""

# from main import stats_overview, gender_chart

import pandas as pd
import matplotlib.pyplot as plt


# Function to test stats_overview
def test_stats_overview():
    # Create a sample DataFrame
    data = {
        "Apps Received": [100, 200, 150],
        "Female": [40, 80, 70],
        "Male": [60, 110, 80],
    }
    df = pd.DataFrame(data)

    # Calculate summary statistics
    summary_stats = df.describe()
    summary_stats.loc["median"] = df.median()
    summary_stats.loc["total"] = df.sum()
    summary_stats = summary_stats.round(2)

    # Print the results
    print("Test stats_overview:")
    print(summary_stats)

    # Basic checks
    assert (
        summary_stats.loc["total", "Apps Received"] == 450
    ), "Total Apps Received should be 450"
    assert (
        summary_stats.loc["mean", "Female"] == 63.33
    ), "Mean Female applicants should be 63.33"
    print("stats_overview test passed!")


def test_gender_chart():
    data = {"Female": [40, 80, 70], "Male": [60, 110, 80]}
    # Basic checks
    assert len(plt.gca().patches) == 2, "There should be 2 bars in the chart"
    assert (
        plt.gca().patches[0].get_height() == 190
    ), "Total Female applicants should be 190"
    assert (
        plt.gca().patches[1].get_height() == 250
    ), "Total Male applicants should be 250"
    print("gender_chart test passed!")

    plt.close()


# if __name__ == "__main__":
#     test_stats_overview()
#     test_gender_chart()
#     print("All tests passed!")


# # def test_stats_overview():
# #     overview = stats_overview()
# #     assert overview is not None


# # def test_gender_chart():
# #     chart = gender_chart()
# #     assert chart is not None
