# syn_vc
version control for Synapse projects implemented in Python

#Installation
```
git clone https://github.com/pvtodorov/syn_vc.git
cd syn_vc
pip install -e .
```

#Guide
- Make sure you are logged into Synapse via the client. This can be done with.
```
synapse login -u USERNAME -p PASSWORD --rememberMe
```
- Navigate to the folder containing your project. To upload your files:
```
syn-upload LOCAL_FOLDER PROJECT_SYNID
```
