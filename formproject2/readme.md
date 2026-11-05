python -m django --version

python -m django startproject formproject2

cd formproject2
py manage.py startapp myapp



1. Open your browser and navigate to: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
2. Fill out the feedback form (Name, Age, Email, Feedback) and click **Submit**.
3. You will receive the confirmation message: **"Response Recorded"**.
4. Verify the stored data in MySQL:
   ```sql
   USE stud;
   SELECT * FROM myapp_student;
   ```


python populate.py
pip install faker 

## problem
    raise AppRegistryNotReady("Apps aren't loaded yet.")
django.core.exceptions.AppRegistryNotReady: Apps aren't loaded yet.
## solutin
make the migrations 

