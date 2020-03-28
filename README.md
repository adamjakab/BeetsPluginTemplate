[![Build Status](https://travis-ci.org/adamjakab/BeetsPluginTemplate.svg?branch=master)](https://travis-ci.org/adamjakab/BeetsPluginTemplate)
[![Coverage Status](https://coveralls.io/repos/github/adamjakab/BeetsPluginTemplate/badge.svg?branch=master)](https://coveralls.io/github/adamjakab/BeetsPluginTemplate?branch=master)
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE.txt)


# Beets Plugin Template

An empty template structure to speed up plugin development.


## Usage:

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

### 4. Change the name of the plugin folder
Change the name folder `template` under `beetsplug` to `PLUGIN_NAME`

### 5. Change code in: `setup.py`
Substitute all occurrences of `template` with `PLUGIN_NAME`

### 6. Change code in: `beetsplug/template/__init__.py`
- Substitute all occurrences of `template` with `PLUGIN_NAME`
- Change class name `TemplatePlugin` to `<PLUGIN_NAME>Plugin`
- Change class name `TemplateCommand` to `<PLUGIN_NAME>Command`

### 7. Change code in: `beetsplug/template/command.py`
- Substitute all occurrences of `template` with `PLUGIN_NAME`
- Change class name `TemplateCommand` to `<PLUGIN_NAME>Command`

### 8. Change code in: `beetsplug/template/common.py`
- Substitute all occurrences of `template` with `PLUGIN_NAME`

### 9. Change copyright headers
In all files, in the copyright header, change:
- `<AUTHOR>` to your name
- `<EMAIL>` to your e-mail address

### 10. Add the path of your plugin to your beets configuration
```yaml
pluginpath:
    - PLUGIN_DIR/beetsplug/
```

### 11. Add your plugin to the list of enabled plugins
```yaml
plugins:
    - PLUGIN_NAME
```

### 12. Tests
- Substitute all occurrences of `template` with `PLUGIN_NAME`
- Change class name `TemplatePlugin` to `<PLUGIN_NAME>Plugin` in `test/helper.py`
- Install nosetests: `pip install nose`
- Run the tests with `nosetests` - all tests should pass and you should get 100% coverage. Keep it that way ;)

### 13. Run the command
Run the command with: `beet template`.


## Now, it's your turn
The [plugin development documentation](https://beets.readthedocs.io/en/stable/dev/plugins.html) is a good place to start.