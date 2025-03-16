# synoPhoto

Script for tidy tools for synology DS214.
Pictures and videos are uploaded to the server into `/var/services/homes/*/photo/` folder using DSfile app and moved to
`/var/services/photo` with the following structure `photo/year/month/` by this script.

## Environment setup

Export free mobile user id and password.
Credentials are stored in `on_boot.sh` script, run at the server boot.

```shell
echo "# Free Mobile credentials" >> on_boot.sh
echo export FREEUSER="'freeuser'" >> on_boot.sh
echo export FREEPWD="'pwd'" >> on_boot.sh
````

Build the env and test the installation.
```shell
python3 -m venv venv & \
source venv/bin/activate & \
python3 -m pip install --upgrade pip & \
pip install git+https://github.com/nakmuaycoder/synoPhoto.git & \
# Test the install
sms --user=$FREEUSER --password=$FREEPWD --message="Config OK"
```

## Run the script

```shell
python3 synoPhoto \
    --root_path=/volume1/homes/*/photo  \
    --image --video \
    --pixel --samsung
    --path_dest=/volume1/photo/ \
    --free_mobile_user=$FREEUSER
    --free_mobile_password=$FREEPWD
```