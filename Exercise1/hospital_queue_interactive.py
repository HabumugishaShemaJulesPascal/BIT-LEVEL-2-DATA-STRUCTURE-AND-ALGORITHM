# hospital_queue_interactive.py
# Demonstration script for "Hospital Patient Queue" tasks with interactive input.

from array import array

# 1) INTEGERS: ask the user for queue counts
queue_counts = []
n = int(input("How many departments? "))
for i in range(n):
    val = int(input(f"Enter patient queue count for department {i+1}: "))
    queue_counts.append(val)

total_patients = sum(queue_counts)
average_patients = total_patients / len(queue_counts) if queue_counts else 0
min_queue = min(queue_counts) if queue_counts else 0
max_queue = max(queue_counts) if queue_counts else 0

print("\n=== INTEGERS: Queue Stats ===")
print(f"Total patients across departments: {total_patients}")
print(f"Average patients per department: {average_patients:.2f}")
print(f"Minimum queue length: {min_queue}, Maximum queue length: {max_queue}")
print()

# 2) STRINGS: formatted report
report = (
    "Hospital Patient Queue Report\n"
    f"Departments counted: {len(queue_counts)}\n"
    f"Total patients: {total_patients}\n"
    f"Average queue length: {average_patients:.2f}\n"
    f"Queue lengths: {queue_counts}\n"
)
print("=== FORMATTED STRING REPORT ===")
print(report)
summary_total = f"Summary total: {total_patients} patients in {len(queue_counts)} departments."
summary_avg = f"Summary average: {average_patients:.1f} patients/department."
print(summary_total)
print(summary_avg)
print()

# 3) BOOLEANS: threshold check + compound boolean
threshold = int(input("Enter threshold to compare average with: "))
print("=== BOOLEAN THRESHOLD CHECK ===")
if average_patients > threshold:
    print("Status: Above Standard")
else:
    print("Status: Below Standard")

compound_condition = (average_patients > threshold) and (max_queue > threshold * 1.5)
if compound_condition:
    print("Alert: Average above threshold AND at least one queue is significantly larger than the threshold.")
elif (average_patients > threshold) or (max_queue > threshold * 1.5):
    print("Notice: Either average is above threshold OR there is at least one significantly large queue.")
else:
    print("All queues are within normal limits.")
print()

# 4) LISTS: maintain patient list, add, remove by condition, sort, display
patients = []
m = int(input("How many patient names to enter initially? "))
for i in range(m):
    patients.append(input(f"Enter patient name {i+1}: "))

print("\n=== LISTS: Patient Names ===")
print("Original list (unsorted):", patients)
print("Original list (sorted):", sorted(patients))

# Add a new patient
new_patient = input("Enter a new patient to add: ")
patients.append(new_patient)
print("After adding:", patients)

# Remove a patient whose name starts with a chosen letter
letter = input("Enter a letter to remove first patient whose name starts with it: ").lower()
to_remove = next((p for p in patients if p.lower().startswith(letter)), None)
if to_remove:
    patients.remove(to_remove)
    print(f"Removed patient based on condition (starts with '{letter.upper()}'): {to_remove}")
else:
    print("No patient met the removal condition.")

patients.sort()
print("Modified list (sorted):", patients)
print()

# 5) ARRAYS: use array module for a fixed-size numeric subset; compare sums
arr_subset = array('i', queue_counts[:3])  # fixed-type array (first 3 queue values)
print("=== ARRAYS: Fixed-size numeric subset ===")
print("Array contents (as list):", arr_subset.tolist())
sum_array = sum(arr_subset)
sum_list_subset = sum(queue_counts[:3])
print(f"Sum of array subset: {sum_array}")
print(f"Sum of equivalent list subset: {sum_list_subset}")
print("Are the sums equal?", sum_array == sum_list_subset)
print()

# 6) DICTIONARIES: list of dicts with id, name, value. Update one, delete another, compute total.
print("=== DICTIONARIES: Patient Records ===")
k = int(input("How many patient records to create? "))
patient_records = []
for i in range(k):
    pid = i + 1
    pname = input(f"Enter name for patient id={pid}: ")
    pvalue = int(input(f"Enter value (e.g., bill or score) for {pname}: "))
    patient_records.append({'id': pid, 'name': pname, 'value': pvalue})

print("Original records:")
for rec in patient_records:
    print(rec)

if patient_records:
    update_id = int(input("Enter id to update its value: "))
    for rec in patient_records:
        if rec['id'] == update_id:
            rec['value'] = int(input("Enter new value: "))
            rec['note'] = 'Updated value'
            print("Updated record:", rec)
            break

delete_id = int(input("Enter id to delete: "))
patient_records = [rec for rec in patient_records if rec['id'] != delete_id]

print("Records after deleting chosen id:")
for rec in patient_records:
    print(rec)

total_value = sum(rec['value'] for rec in patient_records)
print(f"Total of 'value' across remaining records: {total_value}")
