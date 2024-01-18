
import tkinter as tk
from tkinter import ttk, Listbox, END, messagebox

def create_runners_page(notebook):
    runners_page = ttk.Frame(notebook)
    notebook.add(runners_page, text="Runners")

    # Variables for input fields
    first_name_var = tk.StringVar()
    last_name_var = tk.StringVar()
    graduation_year_var = tk.StringVar()
    grade_var = tk.StringVar()
    milesplit_url_var = tk.StringVar()

    # Function to add a runner
    def add_runner():
        first_name = first_name_var.get()
        last_name = last_name_var.get()
        graduation_year = graduation_year_var.get()
        grade = grade_var.get()
        milesplit_url = milesplit_url_var.get()

        # Add your logic here to handle adding a runner (e.g., store in a data structure)
        messagebox.showinfo("Add Runner", f"Runner added:\nFirst Name: {first_name}\nLast Name: {last_name}\nGraduation Year: {graduation_year}\nGrade: {grade}\nMilesplit URL: {milesplit_url}")

    # Function to update a runner
    def update_runner():
        # Add your logic here to handle updating a runner
        messagebox.showinfo("Update Runner", "Runner updated")

    # Function to delete a runner
    def delete_runner():
        # Add your logic here to handle deleting a runner
        messagebox.showinfo("Delete Runner", "Runner deleted")

    # Function to populate input fields when a runner is selected
    def on_runner_select(event):
        selected_index = runners_listbox.curselection()
        if selected_index:
            selected_runner = runners_listbox.get(selected_index)
            # Add your logic here to retrieve and display information for the selected runner
            # For now, let's just display the selected runner's name in the messagebox
            messagebox.showinfo("Selected Runner", f"Selected Runner: {selected_runner}")

    # Labels and entry widgets for runner details
    tk.Label(runners_page, text="First Name:", font=("Helvetica", 14)).grid(row=0, column=1, sticky="w", pady=10)
    tk.Entry(runners_page, textvariable=first_name_var, font=("Helvetica", 14)).grid(row=0, column=2, pady=10)

    tk.Label(runners_page, text="Last Name:", font=("Helvetica", 14)).grid(row=1, column=1, sticky="w", pady=10)
    tk.Entry(runners_page, textvariable=last_name_var, font=("Helvetica", 14)).grid(row=1, column=2, pady=10)

    tk.Label(runners_page, text="Graduation Year:", font=("Helvetica", 14)).grid(row=2, column=1, sticky="w", pady=10)
    tk.Entry(runners_page, textvariable=graduation_year_var, font=("Helvetica", 14)).grid(row=2, column=2, pady=10)

    tk.Label(runners_page, text="Grade (9th-12th):", font=("Helvetica", 14)).grid(row=3, column=1, sticky="w", pady=10)
    tk.Entry(runners_page, textvariable=grade_var, font=("Helvetica", 14)).grid(row=3, column=2, pady=10)

    tk.Label(runners_page, text="Milesplit URL:", font=("Helvetica", 14)).grid(row=4, column=1, sticky="w", pady=10)
    tk.Entry(runners_page, textvariable=milesplit_url_var, font=("Helvetica", 14)).grid(row=4, column=2, pady=10)

    # Listbox to display runner names
    runners_listbox = tk.Listbox(runners_page, selectmode=tk.SINGLE, font=("Helvetica", 14))
    runners_listbox.grid(row=0, column=0, rowspan=5, sticky="ns", padx=10)
    runners_listbox.insert(tk.END, "Runner 1", "Runner 2", "Runner 3")  # You can populate the list with actual runner names

    # Bind the on_runner_select function to the listbox selection event
    runners_listbox.bind("<<ListboxSelect>>", on_runner_select)

    # Buttons for add, update, delete
    tk.Button(runners_page, text="Add", command=add_runner, font=("Helvetica", 14)).grid(row=5, column=1, pady=20)
    tk.Button(runners_page, text="Update", command=update_runner, font=("Helvetica", 14)).grid(row=5, column=2, pady=20)
    tk.Button(runners_page, text="Delete", command=delete_runner, font=("Helvetica", 14)).grid(row=5, column=3, pady=20)


def create_roster_page(notebook):
    roster_page = ttk.Frame(notebook)
    notebook.add(roster_page, text="Roster")

    # Variables for main list and male/female categories
    runners_list = ["Runner 1", "Runner 2", "Runner 3"]  # Replace with your actual list of runners
    male_runners = []
    female_runners = []

    # Function to create roster
    def create_roster():
        # Add your logic here to handle creating the roster
        messagebox.showinfo("Create Roster", f"Roster created:\nMale: {male_runners}\nFemale: {female_runners}")

    # Function to update categories when a runner is dragged
    def update_categories(event, category_listbox, category_list):
        selected_index = category_listbox.nearest(event.y)
        if selected_index != -1:
            selected_runner = category_listbox.get(selected_index)
            # Add your logic here to update the categories based on the selected runner
            # For now, let's just move the runner to the corresponding category
            if selected_runner in category_list:
                category_listbox.delete(selected_index)
                category_list.remove(selected_runner)
                main_listbox.insert(END, selected_runner)

    # Function to determine gender (replace this with your actual logic)
    def determine_gender(runner):
        # Add your logic to determine the gender of the runner
        # For now, let's randomly assign gender based on the length of the runner's name
        return "Male" if len(runner) % 2 == 0 else "Female"

    # Main listbox to display all runners
    main_listbox = Listbox(roster_page, selectmode=tk.SINGLE, font=("Helvetica", 14))
    main_listbox.grid(row=0, column=0, rowspan=5, sticky="ns", padx=10)
    main_listbox.insert(END, *runners_list)

    # Bind the update_categories function to the listbox selection event
    main_listbox.bind("<B1-Motion>", lambda event: update_categories(event, main_listbox, runners_list))

    # Male category listbox
    male_listbox = Listbox(roster_page, selectmode=tk.SINGLE, font=("Helvetica", 14))
    male_listbox.grid(row=0, column=1, sticky="ns", padx=10)
    tk.Label(roster_page, text="Male", font=("Helvetica", 14)).grid(row=0, column=1, pady=10)

    # Bind the update_categories function to the listbox selection event
    male_listbox.bind("<B1-Motion>", lambda event: update_categories(event, male_listbox, male_runners))

    # Female category listbox
    female_listbox = Listbox(roster_page, selectmode=tk.SINGLE, font=("Helvetica", 14))
    female_listbox.grid(row=0, column=2, sticky="ns", padx=10)
    tk.Label(roster_page, text="Female", font=("Helvetica", 14)).grid(row=0, column=2, pady=10)

    # Bind the update_categories function to the listbox selection event
    female_listbox.bind("<B1-Motion>", lambda event: update_categories(event, female_listbox, female_runners))

    # Create Roster button
    tk.Button(roster_page, text="Create Roster", command=create_roster, font=("Helvetica", 14)).grid(row=2, column=1, columnspan=2, pady=20)
def create_race_page(notebook):
    race_page = ttk.Frame(notebook)
    notebook.add(race_page, text="Race")

    # Variables for races and selected race details
    races_list = ["Race 1", "Race 2", "Race 3"]  # Replace with your actual list of races
    selected_race_details = {}

    # Function to display selected race details
    def display_race_details(selected_race):
        # Add your logic here to retrieve and display details for the selected race
        # For now, let's just display a messagebox with the selected race details
        if selected_race in selected_race_details:
            race_details = selected_race_details[selected_race]
            header = f"{'Runner Name': <20}{'Time': <15}\n{'-'*35}\n"
            details = "\n".join([f"{runner: <20}{time: <15}" for runner, time in race_details.items()])
            selected_race_text.config(state=tk.NORMAL)
            selected_race_text.delete("1.0", tk.END)
            selected_race_text.insert(tk.END, f"Selected Race: {selected_race}\n\n{header}{details}")
            selected_race_text.config(state=tk.DISABLED)

    # Function to add a new race to the list
    def add_race():
        new_race = new_race_entry.get()
        if new_race:
            races_list.append(new_race)
            races_listbox.insert(tk.END, new_race)
            new_race_entry.delete(0, tk.END)  # Clear the entry after adding a new race

    # Function to update selected race details
    def update_selected_race(event):
        selected_index = races_listbox.curselection()
        if selected_index:
            selected_race = races_listbox.get(selected_index)
            # Add your logic here to update the selected race details
            # For now, let's just populate some dummy data
            selected_race_details[selected_race] = {"Runner 1": "12:30", "Runner 2": "13:15", "Runner 3": "11:45"}
            display_race_details(selected_race)

    # Left listbox to display races
    races_listbox = tk.Listbox(race_page, selectmode=tk.SINGLE, font=("Helvetica", 14))
    races_listbox.grid(row=0, column=0, rowspan=5, sticky="ns", padx=10)
    races_listbox.insert(tk.END, *races_list)

    # Bind the update_selected_race function to the listbox selection event
    races_listbox.bind("<ButtonRelease-1>", update_selected_race)

    # Entry box to add a new race
    new_race_entry = tk.Entry(race_page, font=("Helvetica", 14))
    new_race_entry.grid(row=0, column=1, pady=10)
    tk.Button(race_page, text="Add Race", command=add_race, font=("Helvetica", 14)).grid(row=1, column=1, pady=10)

    # Display area for selected race details
    selected_race_label = tk.Label(race_page, text="Selected Race Details", font=("Helvetica", 16, "bold"))
    selected_race_label.grid(row=2, column=1, pady=10)

    # Create a text widget to display the selected race details
    selected_race_text = tk.Text(race_page, wrap="word", width=60, height=15, font=("Helvetica", 14))
    selected_race_text.grid(row=3, column=1, pady=10)

    # Bind the update_selected_race_text function to the listbox selection event
    races_listbox.bind("<ButtonRelease-1>", lambda event: update_selected_race_text(races_listbox.get(races_listbox.curselection())))
    # Bind the clear_selected_race_text function to the listbox selection event
    races_listbox.bind("<ButtonRelease-1>", lambda event: clear_selected_race_text())

    # Function to update the text widget with selected race details
    def update_selected_race_text(selected_race):
        if selected_race in selected_race_details:
            race_details = selected_race_details[selected_race]
            header = f"{'Runner Name': <20}{'Time': <15}\n{'-'*35}\n"
            details = "\n".join([f"{runner: <20}{time: <15}" for runner, time in race_details.items()])
            selected_race_text.config(state=tk.NORMAL)
            selected_race_text.delete("1.0", tk.END)
            selected_race_text.insert(tk.END, f"Selected Race: {selected_race}\n\n{header}{details}")
            selected_race_text.config(state=tk.DISABLED)

    # Function to clear the selected race details
    def clear_selected_race_text():
        selected_race_text.config(state=tk.NORMAL)
        selected_race_text.delete("1.0", tk.END)
        selected_race_text.config(state=tk.DISABLED)

def create_reports_page(notebook):
    reports_page = ttk.Frame(notebook)
    notebook.add(reports_page, text="Reports")

    # Variables for races and runner times
    races_list = ["Race 1", "Race 2", "Race 3"]  # Replace with your actual list of races
    runner_times = {
        "Race 1": {"Runner 1": "12:30", "Runner 2": "13:15", "Runner 3": "11:45"},
        "Race 2": {"Runner 1": "11:45", "Runner 2": "14:00", "Runner 3": "12:30"},
        "Race 3": {"Runner 1": "13:00", "Runner 2": "12:45", "Runner 3": "11:15"}
    }

    # Function to display runner names and times based on the selected race or "All Time"
    def display_runner_times(selected_race):
        if selected_race == "All Time":
            # Display all-time runner names and times
            all_time_details = {runner: [times[race] for race, times in runner_times.items()] for runner in runner_times["Race 1"]}
            header = f"{'Runner Name': <20}{'All Time Times': <30}\n{'-'*50}\n"
            details = "\n".join([f"{runner: <20}{', '.join(times): <30}" for runner, times in all_time_details.items()])
            reports_text.config(state=tk.NORMAL)
            reports_text.delete("1.0", tk.END)
            reports_text.insert(tk.END, f"Selected Report: All Time\n\n{header}{details}")
        elif selected_race in runner_times:
            # Display runner names and times for the selected race
            race_details = runner_times[selected_race]
            header = f"{'Runner Name': <20}{'Time': <15}\n{'-'*35}\n"
            details = "\n".join([f"{runner: <20}{time: <15}" for runner, time in race_details.items()])
            reports_text.config(state=tk.NORMAL)
            reports_text.delete("1.0", tk.END)
            reports_text.insert(tk.END, f"Selected Report: {selected_race}\n\n{header}{details}")
        reports_text.config(state=tk.DISABLED)

    # Dropdown menu for selecting the report type
    report_options = ["All Time"] + races_list
    selected_report_var = tk.StringVar()
    selected_report_var.set(report_options[0])  # Set the default option to "All Time"

    report_dropdown = tk.OptionMenu(reports_page, selected_report_var, *report_options)
    report_dropdown.grid(row=0, column=0, pady=10)

    # Bind the display_runner_times function to the dropdown selection event
    report_dropdown.bind("<Configure>", lambda event: display_runner_times(selected_report_var.get()))

    # Display area for runner names and times
    reports_label = tk.Label(reports_page, text="Runner Times Report", font=("Helvetica", 16, "bold"))
    reports_label.grid(row=1, column=0, pady=10)

    # Create a text widget to display the runner names and times
    reports_text = tk.Text(reports_page, wrap="word", width=60, height=15, font=("Helvetica", 14))
    reports_text.grid(row=2, column=0, pady=10)

    # Function to clear the reports text
    def clear_reports_text():
        reports_text.config(state=tk.NORMAL)
        reports_text.delete("1.0", tk.END)
        reports_text.config(state=tk.DISABLED)

    # Bind the clear_reports_text function to the dropdown selection event
    report_dropdown.bind("<Configure>", lambda event: clear_reports_text())
