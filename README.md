# Beets Plugin Template

An empty template structure to speed up plugin development.


# Usage:

### 1. Decide the name for your plugin. 
You will need this to name folders and values inside the code.
In the below instructions the `PLUGIN_NAME` and `PLUGIN_DIR` placeholders will be used. 

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

### 4. setup.py
Substitute all occurrences of `template` with `PLUGIN_NAME`

### 5. beetsplug/template/__init__.py
- Substitute all occurrences of `template` with `PLUGIN_NAME`
- Change class name `TemplatePlugin` to `<PLUGIN_NAME>Plugin`
- Change class name `TemplateCommand` to `<PLUGIN_NAME>Command`

### 6. beetsplug/template/command.py
- Substitute all occurrences of `template` with `PLUGIN_NAME`
- Change class name `TemplateCommand` to `<PLUGIN_NAME>Command`

### 7. beetsplug/template/common.py
- Substitute all occurrences of `template` with `PLUGIN_NAME`

### 8. Add the path of your plugin to your beets configuration
```yaml
pluginpath:
    - PLUGIN_DIR/beetsplug/
```

### 9. Add your plugin to the list of enabled plugins
```yaml
plugins:
    - PLUGIN_NAME
```

