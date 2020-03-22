# Beets Plugin Template

An empty template structure to speed up plugin development.


# Usage:

### 1. Decide the name for your plugin. 
You will need this to name folders and values inside the code.
For the sake of the instructions i will use the `PLUGIN_NAME` and `PLUGIN_DIR` placeholders. 

### 2. Clone the repository
```bash
git clone https://github.com/adamjakab/BeetsPluginTemplate.git PLUGIN_DIR
```

### 3. Reset git
```bash
cd PLUGIN_DIR
rm -rf .git
git init
```




### 99. Add the path of your plugin to your beets configuration
```yaml
pluginpath:
    - PLUGIN_DIR
```


### 100. Add your plugin to the list of enabled plugins
```yaml
plugins:
    - PLUGIN_NAME
```

