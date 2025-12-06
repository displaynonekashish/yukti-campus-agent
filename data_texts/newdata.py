import os

# Define the root directory (as seen in your vscode)
BASE_DIR = "data_texts"

# Data Content Dictionary
# (I have kept the content same as previous, just mapping to new paths)

files_map = {
    # ---------------------------------------------------------
    # LOCATION: ACADEMICS > cells > academic-section
    # ---------------------------------------------------------
    os.path.join(BASE_DIR, "ACADEMICS", "cells", "academic-section", "grading_credits_honours.txt"): """Subject: CBCS System, Grading, Credits, and Honours Degree
Keywords: grading system, sgpa, cgpa, credits, honors, passing marks, practical pass, mooc, nptel

1. The Choice Based Credit System (CBCS):
   - Definition: Academic weight is measured in Credits.
   - Credit Formula:
     * 1 Hour Lecture (L) = 1 Credit
     * 1 Hour Tutorial (T) = 1 Credit
     * 1 Hour Practical (P) = 0.5 Credit (Labs have half weightage).

2. Passing Standards (The 40-50 Rule):
   - Theory Pass Marks: 40% (Grade P).
   - Practical/Lab Pass Marks: 50%.
   - Consequence: A student scoring 45% in Theory passes, but 45% in a Lab is a FAIL.

3. Grading Table (BTU/ECA Standard):
   - O (10.0), A+ (9.0), A (8.5), B+ (8.0), B (7.5), C (7.0), P (6.5).
   - F (Fail): <40% (Theory) or <50% (Practical).

4. B.Tech Honours Degree:
   - Requirement: Earn 20 Extra Credits beyond standard 166 via MOOCs (NPTEL/SWAYAM).

5. Degree Division:
   - Distinction: CGPA >= 7.50 (First attempt).
   - First Division: 6.50 - 7.50.
   - Second Division: 5.50 - 6.50.""",

    os.path.join(BASE_DIR, "ACADEMICS", "cells", "academic-section", "attendance_rules.txt"): """Subject: Attendance Mandates, Detention, and Condonation
Keywords: attendance, 75%, detention, medical leave, condonation

1. The 75% Statutory Mandate:
   - Rule: Minimum 75% attendance required to appear in exams.
   - Separation Logic: Theory and Practical attendance are calculated SEPARATELY.

2. Detention Protocol:
   - Process: Below 75% = "Detained" = No Admit Card for that subject.

3. Medical Leave & Condonation:
   - Reality: Medical certificates allow the Principal to "Condone" (Forgive) shortage only down to ~60-65%.
   - Procedure: Submit Medical Certificate (Govt Doctor) to Proctor Section immediately upon return.""",

    os.path.join(BASE_DIR, "ACADEMICS", "cells", "academic-section", "exam_backlog_rules.txt"): """Subject: Examination Scheme, Backlogs, Mercy Chance, and Revaluation
Keywords: mid term, end term, back exam, mercy chance, revaluation, odd even rule

1. Evaluation Scheme:
   - Internal (20-30%): Mid-Terms + Assignments.
   - External (70-80%): University End-Term.

2. Backlogs (Failures):
   - "Odd-Even" Rule: Odd Sem Backs (1,3,5,7) held in Winter; Even Sem Backs (2,4,6,8) held in Summer.
   - Fee: ~Rs. 600-800 per subject.

3. Revaluation:
   - Allowed for max 4 Theory papers.
   - Copy View: Pay (~Rs. 1000) to see your checked answer sheet.""",

    # ---------------------------------------------------------
    # LOCATION: ACADEMICS > cells > first-year
    # ---------------------------------------------------------
    os.path.join(BASE_DIR, "ACADEMICS", "cells", "first-year", "branch_change_rules.txt"): """Subject: Branch Change Policy and Fee Implications
Keywords: branch change, slide, sfs fee, gas fee

1. The "Golden Window":
   - Timing: Only at the start of III Semester (2nd Year).

2. Eligibility:
   - Must pass 1st Year in First Attempt (Zero Backlogs).
   - Min SGPA >= 5.50.

3. The "Golden Handcuffs" (Fee Rule):
   - GAS to SFS: You pay Higher SFS Fee.
   - SFS to GAS: You CONTINUE paying Higher SFS Fee.
   - Rule: You cannot leave a branch if strength falls below 75%.""",

    # ---------------------------------------------------------
    # LOCATION: ADMINISTRATION > CELLS > central-library
    # ---------------------------------------------------------
    os.path.join(BASE_DIR, "ADMINISTRATION", "CELLS", "central-library", "library_rules_services.txt"): """Subject: Library Rules, Book Bank, and Digital Resources
Keywords: library, book bank, fine, sc st book bank

1. Circulation Rules:
   - Limit: 3 Books for 15 Days.
   - Penalty: Late fee charged per day.

2. Social Welfare Book Bank:
   - Beneficiaries: SC/ST students get a full set of books for the ENTIRE semester (Free).
   - Condition: Must return immediately after exams.

3. Digital: Access to National Digital Library (NDL) and SWAYAM MOOCs.""",

    # ---------------------------------------------------------
    # LOCATION: TRAINING_&_PLACEMENTS
    # ---------------------------------------------------------
    os.path.join(BASE_DIR, "TRAINING_&_PLACEMENTS", "tpo_procedures.txt"): """Subject: Training and Placement Procedures (TPO)
Keywords: internship letter, training letter, placement registration, tpo cell, noc

1. Internship/Training Letter (NOC):
   - Requirement: Mandatory 45-60 Days Training after 6th Sem.
   - Process: Download Format -> Fill -> Sign by HOD -> Submit to TPO.

2. Placement Drive Process:
   - Eligibility: Check criteria (e.g., "No active backlogs", "60% throughout").
   - Documents: 2 Resume Copies, Photos, Original Marksheets.

3. Protocol: Visit TPO Cell Post-lunch (2:00 PM - 4:00 PM) with College ID.""",

    # ---------------------------------------------------------
    # LOCATION: STUDENT_CORNER > Student-Procedures
    # ---------------------------------------------------------
    os.path.join(BASE_DIR, "STUDENT_CORNER", "Student-Procedures", "fee_payment_rules.txt"): """Subject: Fee Structure, Online Payment, and Penalties
Keywords: sfs, gas, late fee, registration form, caution money

1. Fee Categories (Approx):
   - SFS: ~Rs. 55k-60k.
   - GAS (Gen Boys): ~Rs. 29.2k.
   - GAS (Girls/SC/ST/TFWS): ~Rs. 21.7k.

2. Payment Process:
   - Portal: erp.ecajmer.ac.in -> Online Fee Payment.
   - CRITICAL: After paying, fill the "Registration Form" on ERP.

3. Late Fees:
   - 15-30 Days Delay: Rs. 500 Fine.
   - 30-45 Days Delay: Rs. 1000 Fine.""",

    os.path.join(BASE_DIR, "STUDENT_CORNER", "Student-Procedures", "daily_admin_procedures.txt"): """Subject: Daily Administrative Procedures (Leave, Bonafide, Scholarships)
Keywords: medical leave, internship noc, scholarship verification, bonafide

1. Medical Leave:
   - Notify Proctor/HOD immediately.
   - Submit: Application + Original Medical Cert + Fitness Cert upon return.

2. Scholarships (Samaj Kalyan / NSP):
   - Trap: Online application is NOT enough.
   - Mandatory: Submit Hard Copy + Income/Caste Cert + Fee Receipt to Scholarship Section.

3. Bonafide Certificate:
   - Application to Chief Proctor + ID Card Copy + Last Fee Receipt.""",

    os.path.join(BASE_DIR, "STUDENT_CORNER", "Student-Procedures", "communication_protocols.txt"): """Subject: How to Write Applications and Approach Faculty
Keywords: application format, how to talk, hod, principal

1. Hierarchy:
   - Chain: Advisor -> HOD -> Proctor/Principal.

2. Application Format:
   - To: The Principal / HOD.
   - Body: "Respected Sir, I am [Name], [Branch], [Year]..."
   - Closing: "Yours Obediently," Name, Roll No.

3. Email Etiquette:
   - Subject: [Batch] | [Branch] | [Issue].""",

    os.path.join(BASE_DIR, "STUDENT_CORNER", "Student-Procedures", "exit_degree_procedures.txt"): """Subject: No Dues, Degree, TC, and Exit Rules
Keywords: no dues, degree, tc, migration, caution money, btu, rtu

1. Transfer Certificate (TC) & Caution Money:
   - Requirement: "No Dues Certificate" (Signatures from Library, Sports, Warden, Labs, Accounts).
   - Refund: Submit No Dues + Original Fee Receipt + Passbook Copy to Accounts.

2. Migration & Degree:
   - Pre-2018 Batches: Apply at RTU (Kota) website.
   - 2018+ Batches: Apply at BTU (Bikaner) website.
   - Provisional Degree: Collect from college 1-2 months after results.""",

    os.path.join(BASE_DIR, "STUDENT_CORNER", "Student-Procedures", "campus_services_proctor.txt"): """Subject: Transport, Hostel, Anti-Ragging, and ID Cards
Keywords: bus fee, hostel fee, proctor, ragging, id card

1. Transport:
   - Fee: ~Rs. 2500/Sem (Non-Refundable). First-Come-First-Served.

2. Hostel:
   - Total: ~Rs. 15k-18k per semester (Rent + Mess).

3. Proctorial:
   - Ragging: Zero Tolerance.
   - ID Cards: Mandatory. Lost ID requires police report + fee.""",

    # ---------------------------------------------------------
    # LOCATION: STUDENT_CORNER > Student-Activity-Center
    # ---------------------------------------------------------
    os.path.join(BASE_DIR, "STUDENT_CORNER", "Student-Activity-Center", "representation_reimbursement.txt"): """Subject: Student Representation, Hackathons, Reimbursement
Keywords: reimbursement, od, on duty, hackathon, funding

1. The Golden Rule (Pre-Approval):
   - Apply 7-10 days BEFORE event.
   - Submit: Application to Principal (via HOD) + Event Brochure + Budget.

2. On Duty (OD):
   - Submit "Joining Report" + Certificate Copy upon return.

3. Reimbursement:
   - Submit bills within 7 Days.
   - Documents: Original Tickets, Fee Receipt, Certificate Copy, Geotagged Photos, Bank Passbook.""",
}

def create_files_in_hierarchy():
    print(f"🚀 Starting file generation in root: {os.path.abspath(BASE_DIR)}...\n")
    
    for file_path, content in files_map.items():
        # 1. Ensure the directory exists
        directory = os.path.dirname(file_path)
        if not os.path.exists(directory):
            try:
                os.makedirs(directory)
                print(f"📂 Created Directory: {directory}")
            except OSError as e:
                print(f"❌ Error creating directory {directory}: {e}")
                continue

        # 2. Write the file
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"✅ Created File: {file_path}")
        except Exception as e:
            print(f"❌ Error writing file {file_path}: {e}")

if __name__ == "__main__":
    create_files_in_hierarchy()
    print("\n✨ All files have been integrated into your data hierarchy!")