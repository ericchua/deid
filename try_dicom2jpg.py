# dicom2jpg

import dicom2jpg


# convert single DICOM file to jpg format

dicom_img_01 = "D:/deid/Images/Test/DICOM/1-089.dcm"

dicom2jpg.dicom2jpg(dicom_img_01)


# convert all DICOM files in dicom_dir folder to png format, and save to op_dir
# exported filepath is target_root / Today / PatientID_Filetype / StudyDate_StudyTime_Modality_AccNum / Ser_Img.Filetype

dicom_dir = "D:/deid/Images/Test/DICOM/Anonymized_20210725"

op_dir = "D:/deid/Images/Test/PNG"

dicom2jpg.dicom2png(dicom_dir, op_dir)