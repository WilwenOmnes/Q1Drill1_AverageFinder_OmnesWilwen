from pyscript import document

def compute_average(event):
    score1 = document.getElementById("score1").value.strip()
    score2 = document.getElementById("score2").value.strip()

    if not score1 or not score2:
        document.getElementById("average").innerText = "—"
        document.getElementById("result").innerText = "Please enter both scores"
        return

    try:
        score1 = float(score1)
        score2 = float(score2)
        average = (score1 + score2) / 2

        result = "Yes" if average >= 75 else "No"

        document.getElementById("average").innerText = str(round(average, 2))
        document.getElementById("result").innerText = result
    except ValueError:
        document.getElementById("average").innerText = "—"
        document.getElementById("result").innerText = "Invalid input"
