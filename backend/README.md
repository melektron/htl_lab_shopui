For ease of development, this folder can be symlinked to ```/var/www/test/api```. The apache user needs to be able to access all folders (list directory) above them, so they all need o+x permissions:

```bash
sudo ln -s /home/melektron/htl_lab_shopui/backend api
# example permissions for my directory structure
sudo chmod o+x /home /home/melektron /home/melektron/htl_lab_shopui /home/melektron/htl_lab_shopui/backend
```