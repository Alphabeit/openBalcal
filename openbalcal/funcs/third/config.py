from ..third import conf_template
import yaml, os

homefolder = os.path.expanduser("~")
conf_path = "{}{}".format(homefolder, "/openbalcal/config.yml")



def ReadConf(grp, option):
    with open(conf_path, "r") as file:
        conf_file = yaml.safe_load(file)

    return conf_file["config"][grp][option]



def WriteConf(grp, option, new_value):
    with open(conf_path, "r") as file:
        conf_file = yaml.safe_load(file)

    conf_file["config"][grp][option] = new_value

    with open(conf_path, "w") as file:
        yaml.safe_dump(conf_file, file)



def ProvideFiles(file):

    if not os.path.exists("{}{}".format(homefolder, "/openbalcal")):
        os.mkdir("{}{}".format(homefolder, "/openbalcal"))
    if not os.path.exists(file):
        os.mknod(file)

def ProvideFiles_Config():
    ProvideFiles(conf_path)  # config file

def ProvideFiles_DBs():
    ProvideFiles(ReadConf("paths", "topics"))  # topic db
    ProvideFiles(ReadConf("paths", "database"))  # main db



def UpdateOption():
    with open(conf_path, "r") as file:
        conf_exist = yaml.safe_load(file)

    if conf_exist == None:
        conf_exist = 000
    else:
        ver_exist = conf_exist["version"].replace("v", "").replace(".", "")
    
    ver_template = conf_template.Version().replace("v", "").replace(".", "")

    if ver_exist >= ver_template:   # if existing verion of config higher or same as template
        pass  # nothing to do, config file is fine
    else:
        conf_tem = conf_template.Template()   # load template as str
        conf_tem = yaml.safe_load(conf_tem)   # change str to yaml

        # ---------------------------- #
        # start, read existing config
        # if we have already a config seeded, it will be taken over
        for lv1 in conf_tem:
            if lv1 == "version":   # exception, to overwrite version with the newest value
                pass
            elif lv1 in conf_exist:   # looks, if the config already exists

                for lv2 in conf_tem[lv1]:
                    if lv2 in conf_exist[lv1]:   # if exists

                        for lv3 in conf_tem[lv1][lv2]:
                            if lv3 in conf_exist[lv1][lv2]:   # if exists
                                conf_tem[lv1][lv2][lv3] = conf_exist[lv1][lv2][lv3]   # copy the already seeded config

                            else:
                                pass
                    else:
                        pass
            else:   # if not exists, skip
                pass
        # end
        # ---------------------------- #

        with open(conf_path, "w") as file:
            yaml.safe_dump(conf_tem, file)

