# python_project

# TASK 1
1.Develop a web server that exposes on the port 4004 the following endpoints:
  a. /api/health returns a JSON payload containing { "status": "ok" }
  b. /api/mirror?word={word}
    i.Returns a JSON payload containing the transformed input word as follows:
      1. Any lowercase letter must be transformed to be uppercase
      2. Any uppercase letter must be transformed to be lowercase
      3.Any other character should be left as is
      4. A final transformation must be applied so that the whole string is reversed. (’foo’ ⇒ ‘oof’, ‘bar’ ⇒ ‘rab’)
    ii. It saves the the pair <word, mirroredWord> in a database An example: /api/mirror?word=fOoBar25 returns { "transformed": "52RAbOoF" }
A simple test case should be developed so that we make sure that the example provided is treated correctly by the application logic.

<img width="1169" alt="Task 1" src="https://github.com/kangsumang/python_project/assets/108407699/614a2dc8-4612-4636-bf3c-c31ddf2ca716">
<img width="640" alt="Task 1 create db" src="https://github.com/kangsumang/python_project/assets/108407699/ecc66c63-ed79-4f41-9e18-9576f88c0519">
<img width="457" alt="Task 1 create table" src="https://github.com/kangsumang/python_project/assets/108407699/1715a5c0-d0a0-4a6d-941e-e2f3a69ce5be">

# TASK 2
2. Using CI/CD provide jobs for:
  a. Running application tests
  b. (only on main branch) Build a Docker image of the application and push it to a private registry
Please note: The build job should be triggered only if the tests are passing.
<img width="1342" alt="Task 2 Dockerhub image uploaded" src="https://github.com/kangsumang/python_project/assets/108407699/bd27102c-70a6-466f-8a78-2bab3e42a627">

# TASK 3
3. Deploy the application on a VM/K8s cluster (you can use MiniKube for spinning a cluster locally) using helm / kubectl / ansible. The deliverable should:
  a. Use the docker image you just pushed to the registry
  b.Provide an Ingress that listens on port 80 and redirect traffic to the application
<img width="828" alt="Task 3 docker run" src="https://github.com/kangsumang/python_project/assets/108407699/cd449b22-373d-4068-b7c2-a84ccd20a5d9">
<img width="1155" alt="Task 3 docker running" src="https://github.com/kangsumang/python_project/assets/108407699/684fa576-3132-4f54-a8ef-cbef929658aa">
<img width="754" alt="Task 3 pods running" src="https://github.com/kangsumang/python_project/assets/108407699/ef533f1d-be18-48c3-bce3-8dace3e8e48f">
<img width="1071" alt="Task 3 app running" src="https://github.com/kangsumang/python_project/assets/108407699/3c2121ee-0a50-46ec-bd87-8cbb275cd335">

# TASK 4
4. Using Terraform, define the infrastructure to programmatically upload files from the application to a private cloud storage (e.g. Blog Storage, S3 Bucket)
<img width="982" alt="Task 4 terraform upload file" src="https://github.com/kangsumang/python_project/assets/108407699/004fb2d7-2237-4f85-81be-380dc7c8dda8">
<img width="1137" alt="Task 4 s3 file uploaded" src="https://github.com/kangsumang/python_project/assets/108407699/91e254f6-e269-417d-9715-b2bae4458001">

# TASK 5
5. Add an endpoint to your application that listens for POST calls on /api/upload-random. The endpoint logic should create a .txt file with a random number as content of the file and upload it to the cloud storage solution created at point 4.
<img width="1020" alt="Task 5" src="https://github.com/kangsumang/python_project/assets/108407699/c2110a0d-eb52-4975-8a4e-1ea6a4ef696b">
<img width="1342" alt="Task 5 s3" src="https://github.com/kangsumang/python_project/assets/108407699/e782e301-d746-42d5-b216-d56eda16ab41">
