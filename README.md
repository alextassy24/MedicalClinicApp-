# MedicalClinicApp-
Create an app to handle main activities in a hospital involving: Doctors, Patients, Assistants, and Treatments. The system should manage all those activities with the corresponding security in place. 
The ACL will contain 3 main roles: General Manager (has access to all activities),
Doctor (has access to all his patients and can define new ones), and Assistant (has access to allocated patients, one patient can have multiple assistants).
Any management module, like Doctor Management, Patient Management..., should have CRUD capabilities
We have the following components exposed by rest API:
Login
Doctor Management (done by the General manager)
Patient management (done by Doctor or General manager)
Assistant management (done by the General manager)
Treatment management (done by Doctor or General manager)
The treatment recommended by a doctor to a Patient (done by the Doctor)
● Patient assignment to a Assistant (done by Doctor or General manager)
Treatment applied by an Assistant (Assistant only)
• A report containing the list of all the Doctors and the associated patients and a
section for statistics data (JSON) (accessed by the General manager)
A report with all the treatments applied to a Patient (JSON) (accessed by the
General manager or Doctor)
