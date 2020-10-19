// This file is auto-generated from the corresponding file in /dev_mode
/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

require('es6-promise/auto');  // polyfill Promise on IE

import {
  PageConfig
} from '@jupyterlab/coreutils';

// eslint-disable-next-line no-undef
__webpack_public_path__ = PageConfig.getOption('fullStaticUrl') + '/';

// This must be after the public path is set.
// This cannot be extracted because the public path is dynamic.
require('./imports.css');

/**
 * The main entry point for the application.
 */
function main() {
  var JupyterLab = require('@jupyterlab/application').JupyterLab;
  var disabled = [];
  var deferred = [];
  var ignorePlugins = [];
  var register = [];

  // Handle the registered mime extensions.
  var mimeExtensions = [];
  var extension;
  var extMod;
  var plugins = [];
  try {
    extMod = require('@jupyterlab/javascript-extension/');
    extension = extMod.default;

    // Handle CommonJS exports.
    if (!extMod.hasOwnProperty('__esModule')) {
      extension = extMod;
    }

    plugins = Array.isArray(extension) ? extension : [extension];
    plugins.forEach(function(plugin) {
      if (PageConfig.Extension.isDeferred(plugin.id)) {
        deferred.push(plugin.id);
        ignorePlugins.push(plugin.id);
      }
      if (PageConfig.Extension.isDisabled(plugin.id)) {
        disabled.push(plugin.id);
        return;
      }
      mimeExtensions.push(plugin);
    });
  } catch (e) {
    console.error(e);
  }
  try {
    extMod = require('@jupyterlab/json-extension/');
    extension = extMod.default;

    // Handle CommonJS exports.
    if (!extMod.hasOwnProperty('__esModule')) {
      extension = extMod;
    }

    plugins = Array.isArray(extension) ? extension : [extension];
    plugins.forEach(function(plugin) {
      if (PageConfig.Extension.isDeferred(plugin.id)) {
        deferred.push(plugin.id);
        ignorePlugins.push(plugin.id);
      }
      if (PageConfig.Extension.isDisabled(plugin.id)) {
        disabled.push(plugin.id);
        return;
      }
      mimeExtensions.push(plugin);
    });
  } catch (e) {
    console.error(e);
  }
  try {
    extMod = require('@jupyterlab/pdf-extension/');
    extension = extMod.default;

    // Handle CommonJS exports.
    if (!extMod.hasOwnProperty('__esModule')) {
      extension = extMod;
    }

    plugins = Array.isArray(extension) ? extension : [extension];
    plugins.forEach(function(plugin) {
      if (PageConfig.Extension.isDeferred(plugin.id)) {
        deferred.push(plugin.id);
        ignorePlugins.push(plugin.id);
      }
      if (PageConfig.Extension.isDisabled(plugin.id)) {
        disabled.push(plugin.id);
        return;
      }
      mimeExtensions.push(plugin);
    });
  } catch (e) {
    console.error(e);
  }
  try {
    extMod = require('@jupyterlab/vega5-extension/');
    extension = extMod.default;

    // Handle CommonJS exports.
    if (!extMod.hasOwnProperty('__esModule')) {
      extension = extMod;
    }

    plugins = Array.isArray(extension) ? extension : [extension];
    plugins.forEach(function(plugin) {
      if (PageConfig.Extension.isDeferred(plugin.id)) {
        deferred.push(plugin.id);
        ignorePlugins.push(plugin.id);
      }
      if (PageConfig.Extension.isDisabled(plugin.id)) {
        disabled.push(plugin.id);
        return;
      }
      mimeExtensions.push(plugin);
    });
  } catch (e) {
    console.error(e);
  }

  // Handled the registered standard extensions.
  try {
    extMod = require('@jupyterlab/application-extension/');
    extension = extMod.default;

    // Handle CommonJS exports.
    if (!extMod.hasOwnProperty('__esModule')) {
      extension = extMod;
    }

    plugins = Array.isArray(extension) ? extension : [extension];
    plugins.forEach(function(plugin) {
      if (PageConfig.Extension.isDeferred(plugin.id)) {
        deferred.push(plugin.id);
        ignorePlugins.push(plugin.id);
      }
      if (PageConfig.Extension.isDisabled(plugin.id)) {
        disabled.push(plugin.id);
        return;
      }
      register.push(plugin);
    });
  } catch (e) {
    console.error(e);
  }
  try {
    extMod = require('@jupyterlab/apputils-extension/');
    extension = extMod.default;

    // Handle CommonJS exports.
    if (!extMod.hasOwnProperty('__esModule')) {
      extension = extMod;
    }

    plugins = Array.isArray(extension) ? extension : [extension];
    plugins.forEach(function(plugin) {
      if (PageConfig.Extension.isDeferred(plugin.id)) {
        deferred.push(plugin.id);
        ignorePlugins.push(plugin.id);
      }
      if (PageConfig.Extension.isDisabled(plugin.id)) {
        disabled.push(plugin.id);
        return;
      }
      register.push(plugin);
    });
  } catch (e) {
    console.error(e);
  }
  try {
    extMod = require('@jupyterlab/celltags-extension/');
    extension = extMod.default;

    // Handle CommonJS exports.
    if (!extMod.hasOwnProperty('__esModule')) {
      extension = extMod;
    }

    plugins = Array.isArray(extension) ? extension : [extension];
    plugins.forEach(function(plugin) {
      if (PageConfig.Extension.isDeferred(plugin.id)) {
        deferred.push(plugin.id);
        ignorePlugins.push(plugin.id);
      }
      if (PageConfig.Extension.isDisabled(plugin.id)) {
        disabled.push(plugin.id);
        return;
      }
      register.push(plugin);
    });
  } catch (e) {
    console.error(e);
  }
  try {
    extMod = require('@jupyterlab/codemirror-extension/');
    extension = extMod.default;

    // Handle CommonJS exports.
    if (!extMod.hasOwnProperty('__esModule')) {
      extension = extMod;
    }

    plugins = Array.isArray(extension) ? extension : [extension];
    plugins.forEach(function(plugin) {
      if (PageConfig.Extension.isDeferred(plugin.id)) {
        deferred.push(plugin.id);
        ignorePlugins.push(plugin.id);
      }
      if (PageConfig.Extension.isDisabled(plugin.id)) {
        disabled.push(plugin.id);
        return;
      }
      register.push(plugin);
    });
  } catch (e) {
    console.error(e);
  }
  try {
    extMod = require('@jupyterlab/completer-extension/');
    extension = extMod.default;

    // Handle CommonJS exports.
    if (!extMod.hasOwnProperty('__esModule')) {
      extension = extMod;
    }

    plugins = Array.isArray(extension) ? extension : [extension];
    plugins.forEach(function(plugin) {
      if (PageConfig.Extension.isDeferred(plugin.id)) {
        deferred.push(plugin.id);
        ignorePlugins.push(plugin.id);
      }
      if (PageConfig.Extension.isDisabled(plugin.id)) {
        disabled.push(plugin.id);
        return;
      }
      register.push(plugin);
    });
  } catch (e) {
    console.error(e);
  }
  try {
    extMod = require('@jupyterlab/console-extension/');
    extension = extMod.default;

    // Handle CommonJS exports.
    if (!extMod.hasOwnProperty('__esModule')) {
      extension = extMod;
    }

    plugins = Array.isArray(extension) ? extension : [extension];
    plugins.forEach(function(plugin) {
      if (PageConfig.Extension.isDeferred(plugin.id)) {
        deferred.push(plugin.id);
        ignorePlugins.push(plugin.id);
      }
      if (PageConfig.Extension.isDisabled(plugin.id)) {
        disabled.push(plugin.id);
        return;
      }
      register.push(plugin);
    });
  } catch (e) {
    console.error(e);
  }
  try {
    extMod = require('@jupyterlab/csvviewer-extension/');
    extension = extMod.default;

    // Handle CommonJS exports.
    if (!extMod.hasOwnProperty('__esModule')) {
      extension = extMod;
    }

    plugins = Array.isArray(extension) ? extension : [extension];
    plugins.forEach(function(plugin) {
      if (PageConfig.Extension.isDeferred(plugin.id)) {
        deferred.push(plugin.id);
        ignorePlugins.push(plugin.id);
      }
      if (PageConfig.Extension.isDisabled(plugin.id)) {
        disabled.push(plugin.id);
        return;
      }
      register.push(plugin);
    });
  } catch (e) {
    console.error(e);
  }
  try {
    extMod = require('@jupyterlab/docmanager-extension/');
    extension = extMod.default;

    // Handle CommonJS exports.
    if (!extMod.hasOwnProperty('__esModule')) {
      extension = extMod;
    }

    plugins = Array.isArray(extension) ? extension : [extension];
    plugins.forEach(function(plugin) {
      if (PageConfig.Extension.isDeferred(plugin.id)) {
        deferred.push(plugin.id);
        ignorePlugins.push(plugin.id);
      }
      if (PageConfig.Extension.isDisabled(plugin.id)) {
        disabled.push(plugin.id);
        return;
      }
      register.push(plugin);
    });
  } catch (e) {
    console.error(e);
  }
  try {
    extMod = require('@jupyterlab/documentsearch-extension/');
    extension = extMod.default;

    // Handle CommonJS exports.
    if (!extMod.hasOwnProperty('__esModule')) {
      extension = extMod;
    }

    plugins = Array.isArray(extension) ? extension : [extension];
    plugins.forEach(function(plugin) {
      if (PageConfig.Extension.isDeferred(plugin.id)) {
        deferred.push(plugin.id);
        ignorePlugins.push(plugin.id);
      }
      if (PageConfig.Extension.isDisabled(plugin.id)) {
        disabled.push(plugin.id);
        return;
      }
      register.push(plugin);
    });
  } catch (e) {
    console.error(e);
  }
  try {
    extMod = require('@jupyterlab/extensionmanager-extension/');
    extension = extMod.default;

    // Handle CommonJS exports.
    if (!extMod.hasOwnProperty('__esModule')) {
      extension = extMod;
    }

    plugins = Array.isArray(extension) ? extension : [extension];
    plugins.forEach(function(plugin) {
      if (PageConfig.Extension.isDeferred(plugin.id)) {
        deferred.push(plugin.id);
        ignorePlugins.push(plugin.id);
      }
      if (PageConfig.Extension.isDisabled(plugin.id)) {
        disabled.push(plugin.id);
        return;
      }
      register.push(plugin);
    });
  } catch (e) {
    console.error(e);
  }
  try {
    extMod = require('@jupyterlab/filebrowser-extension/');
    extension = extMod.default;

    // Handle CommonJS exports.
    if (!extMod.hasOwnProperty('__esModule')) {
      extension = extMod;
    }

    plugins = Array.isArray(extension) ? extension : [extension];
    plugins.forEach(function(plugin) {
      if (PageConfig.Extension.isDeferred(plugin.id)) {
        deferred.push(plugin.id);
        ignorePlugins.push(plugin.id);
      }
      if (PageConfig.Extension.isDisabled(plugin.id)) {
        disabled.push(plugin.id);
        return;
      }
      register.push(plugin);
    });
  } catch (e) {
    console.error(e);
  }
  try {
    extMod = require('@jupyterlab/fileeditor-extension/');
    extension = extMod.default;

    // Handle CommonJS exports.
    if (!extMod.hasOwnProperty('__esModule')) {
      extension = extMod;
    }

    plugins = Array.isArray(extension) ? extension : [extension];
    plugins.forEach(function(plugin) {
      if (PageConfig.Extension.isDeferred(plugin.id)) {
        deferred.push(plugin.id);
        ignorePlugins.push(plugin.id);
      }
      if (PageConfig.Extension.isDisabled(plugin.id)) {
        disabled.push(plugin.id);
        return;
      }
      register.push(plugin);
    });
  } catch (e) {
    console.error(e);
  }
  try {
    extMod = require('@jupyterlab/help-extension/');
    extension = extMod.default;

    // Handle CommonJS exports.
    if (!extMod.hasOwnProperty('__esModule')) {
      extension = extMod;
    }

    plugins = Array.isArray(extension) ? extension : [extension];
    plugins.forEach(function(plugin) {
      if (PageConfig.Extension.isDeferred(plugin.id)) {
        deferred.push(plugin.id);
        ignorePlugins.push(plugin.id);
      }
      if (PageConfig.Extension.isDisabled(plugin.id)) {
        disabled.push(plugin.id);
        return;
      }
      register.push(plugin);
    });
  } catch (e) {
    console.error(e);
  }
  try {
    extMod = require('@jupyterlab/htmlviewer-extension/');
    extension = extMod.default;

    // Handle CommonJS exports.
    if (!extMod.hasOwnProperty('__esModule')) {
      extension = extMod;
    }

    plugins = Array.isArray(extension) ? extension : [extension];
    plugins.forEach(function(plugin) {
      if (PageConfig.Extension.isDeferred(plugin.id)) {
        deferred.push(plugin.id);
        ignorePlugins.push(plugin.id);
      }
      if (PageConfig.Extension.isDisabled(plugin.id)) {
        disabled.push(plugin.id);
        return;
      }
      register.push(plugin);
    });
  } catch (e) {
    console.error(e);
  }
  try {
    extMod = require('@jupyterlab/hub-extension/');
    extension = extMod.default;

    // Handle CommonJS exports.
    if (!extMod.hasOwnProperty('__esModule')) {
      extension = extMod;
    }

    plugins = Array.isArray(extension) ? extension : [extension];
    plugins.forEach(function(plugin) {
      if (PageConfig.Extension.isDeferred(plugin.id)) {
        deferred.push(plugin.id);
        ignorePlugins.push(plugin.id);
      }
      if (PageConfig.Extension.isDisabled(plugin.id)) {
        disabled.push(plugin.id);
        return;
      }
      register.push(plugin);
    });
  } catch (e) {
    console.error(e);
  }
  try {
    extMod = require('@jupyterlab/imageviewer-extension/');
    extension = extMod.default;

    // Handle CommonJS exports.
    if (!extMod.hasOwnProperty('__esModule')) {
      extension = extMod;
    }

    plugins = Array.isArray(extension) ? extension : [extension];
    plugins.forEach(function(plugin) {
      if (PageConfig.Extension.isDeferred(plugin.id)) {
        deferred.push(plugin.id);
        ignorePlugins.push(plugin.id);
      }
      if (PageConfig.Extension.isDisabled(plugin.id)) {
        disabled.push(plugin.id);
        return;
      }
      register.push(plugin);
    });
  } catch (e) {
    console.error(e);
  }
  try {
    extMod = require('@jupyterlab/inspector-extension/');
    extension = extMod.default;

    // Handle CommonJS exports.
    if (!extMod.hasOwnProperty('__esModule')) {
      extension = extMod;
    }

    plugins = Array.isArray(extension) ? extension : [extension];
    plugins.forEach(function(plugin) {
      if (PageConfig.Extension.isDeferred(plugin.id)) {
        deferred.push(plugin.id);
        ignorePlugins.push(plugin.id);
      }
      if (PageConfig.Extension.isDisabled(plugin.id)) {
        disabled.push(plugin.id);
        return;
      }
      register.push(plugin);
    });
  } catch (e) {
    console.error(e);
  }
  try {
    extMod = require('@jupyterlab/launcher-extension/');
    extension = extMod.default;

    // Handle CommonJS exports.
    if (!extMod.hasOwnProperty('__esModule')) {
      extension = extMod;
    }

    plugins = Array.isArray(extension) ? extension : [extension];
    plugins.forEach(function(plugin) {
      if (PageConfig.Extension.isDeferred(plugin.id)) {
        deferred.push(plugin.id);
        ignorePlugins.push(plugin.id);
      }
      if (PageConfig.Extension.isDisabled(plugin.id)) {
        disabled.push(plugin.id);
        return;
      }
      register.push(plugin);
    });
  } catch (e) {
    console.error(e);
  }
  try {
    extMod = require('@jupyterlab/logconsole-extension/');
    extension = extMod.default;

    // Handle CommonJS exports.
    if (!extMod.hasOwnProperty('__esModule')) {
      extension = extMod;
    }

    plugins = Array.isArray(extension) ? extension : [extension];
    plugins.forEach(function(plugin) {
      if (PageConfig.Extension.isDeferred(plugin.id)) {
        deferred.push(plugin.id);
        ignorePlugins.push(plugin.id);
      }
      if (PageConfig.Extension.isDisabled(plugin.id)) {
        disabled.push(plugin.id);
        return;
      }
      register.push(plugin);
    });
  } catch (e) {
    console.error(e);
  }
  try {
    extMod = require('@jupyterlab/mainmenu-extension/');
    extension = extMod.default;

    // Handle CommonJS exports.
    if (!extMod.hasOwnProperty('__esModule')) {
      extension = extMod;
    }

    plugins = Array.isArray(extension) ? extension : [extension];
    plugins.forEach(function(plugin) {
      if (PageConfig.Extension.isDeferred(plugin.id)) {
        deferred.push(plugin.id);
        ignorePlugins.push(plugin.id);
      }
      if (PageConfig.Extension.isDisabled(plugin.id)) {
        disabled.push(plugin.id);
        return;
      }
      register.push(plugin);
    });
  } catch (e) {
    console.error(e);
  }
  try {
    extMod = require('@jupyterlab/markdownviewer-extension/');
    extension = extMod.default;

    // Handle CommonJS exports.
    if (!extMod.hasOwnProperty('__esModule')) {
      extension = extMod;
    }

    plugins = Array.isArray(extension) ? extension : [extension];
    plugins.forEach(function(plugin) {
      if (PageConfig.Extension.isDeferred(plugin.id)) {
        deferred.push(plugin.id);
        ignorePlugins.push(plugin.id);
      }
      if (PageConfig.Extension.isDisabled(plugin.id)) {
        disabled.push(plugin.id);
        return;
      }
      register.push(plugin);
    });
  } catch (e) {
    console.error(e);
  }
  try {
    extMod = require('@jupyterlab/mathjax2-extension/');
    extension = extMod.default;

    // Handle CommonJS exports.
    if (!extMod.hasOwnProperty('__esModule')) {
      extension = extMod;
    }

    plugins = Array.isArray(extension) ? extension : [extension];
    plugins.forEach(function(plugin) {
      if (PageConfig.Extension.isDeferred(plugin.id)) {
        deferred.push(plugin.id);
        ignorePlugins.push(plugin.id);
      }
      if (PageConfig.Extension.isDisabled(plugin.id)) {
        disabled.push(plugin.id);
        return;
      }
      register.push(plugin);
    });
  } catch (e) {
    console.error(e);
  }
  try {
    extMod = require('@jupyterlab/notebook-extension/');
    extension = extMod.default;

    // Handle CommonJS exports.
    if (!extMod.hasOwnProperty('__esModule')) {
      extension = extMod;
    }

    plugins = Array.isArray(extension) ? extension : [extension];
    plugins.forEach(function(plugin) {
      if (PageConfig.Extension.isDeferred(plugin.id)) {
        deferred.push(plugin.id);
        ignorePlugins.push(plugin.id);
      }
      if (PageConfig.Extension.isDisabled(plugin.id)) {
        disabled.push(plugin.id);
        return;
      }
      register.push(plugin);
    });
  } catch (e) {
    console.error(e);
  }
  try {
    extMod = require('@jupyterlab/rendermime-extension/');
    extension = extMod.default;

    // Handle CommonJS exports.
    if (!extMod.hasOwnProperty('__esModule')) {
      extension = extMod;
    }

    plugins = Array.isArray(extension) ? extension : [extension];
    plugins.forEach(function(plugin) {
      if (PageConfig.Extension.isDeferred(plugin.id)) {
        deferred.push(plugin.id);
        ignorePlugins.push(plugin.id);
      }
      if (PageConfig.Extension.isDisabled(plugin.id)) {
        disabled.push(plugin.id);
        return;
      }
      register.push(plugin);
    });
  } catch (e) {
    console.error(e);
  }
  try {
    extMod = require('@jupyterlab/running-extension/');
    extension = extMod.default;

    // Handle CommonJS exports.
    if (!extMod.hasOwnProperty('__esModule')) {
      extension = extMod;
    }

    plugins = Array.isArray(extension) ? extension : [extension];
    plugins.forEach(function(plugin) {
      if (PageConfig.Extension.isDeferred(plugin.id)) {
        deferred.push(plugin.id);
        ignorePlugins.push(plugin.id);
      }
      if (PageConfig.Extension.isDisabled(plugin.id)) {
        disabled.push(plugin.id);
        return;
      }
      register.push(plugin);
    });
  } catch (e) {
    console.error(e);
  }
  try {
    extMod = require('@jupyterlab/settingeditor-extension/');
    extension = extMod.default;

    // Handle CommonJS exports.
    if (!extMod.hasOwnProperty('__esModule')) {
      extension = extMod;
    }

    plugins = Array.isArray(extension) ? extension : [extension];
    plugins.forEach(function(plugin) {
      if (PageConfig.Extension.isDeferred(plugin.id)) {
        deferred.push(plugin.id);
        ignorePlugins.push(plugin.id);
      }
      if (PageConfig.Extension.isDisabled(plugin.id)) {
        disabled.push(plugin.id);
        return;
      }
      register.push(plugin);
    });
  } catch (e) {
    console.error(e);
  }
  try {
    extMod = require('@jupyterlab/shortcuts-extension/');
    extension = extMod.default;

    // Handle CommonJS exports.
    if (!extMod.hasOwnProperty('__esModule')) {
      extension = extMod;
    }

    plugins = Array.isArray(extension) ? extension : [extension];
    plugins.forEach(function(plugin) {
      if (PageConfig.Extension.isDeferred(plugin.id)) {
        deferred.push(plugin.id);
        ignorePlugins.push(plugin.id);
      }
      if (PageConfig.Extension.isDisabled(plugin.id)) {
        disabled.push(plugin.id);
        return;
      }
      register.push(plugin);
    });
  } catch (e) {
    console.error(e);
  }
  try {
    extMod = require('@jupyterlab/statusbar-extension/');
    extension = extMod.default;

    // Handle CommonJS exports.
    if (!extMod.hasOwnProperty('__esModule')) {
      extension = extMod;
    }

    plugins = Array.isArray(extension) ? extension : [extension];
    plugins.forEach(function(plugin) {
      if (PageConfig.Extension.isDeferred(plugin.id)) {
        deferred.push(plugin.id);
        ignorePlugins.push(plugin.id);
      }
      if (PageConfig.Extension.isDisabled(plugin.id)) {
        disabled.push(plugin.id);
        return;
      }
      register.push(plugin);
    });
  } catch (e) {
    console.error(e);
  }
  try {
    extMod = require('@jupyterlab/tabmanager-extension/');
    extension = extMod.default;

    // Handle CommonJS exports.
    if (!extMod.hasOwnProperty('__esModule')) {
      extension = extMod;
    }

    plugins = Array.isArray(extension) ? extension : [extension];
    plugins.forEach(function(plugin) {
      if (PageConfig.Extension.isDeferred(plugin.id)) {
        deferred.push(plugin.id);
        ignorePlugins.push(plugin.id);
      }
      if (PageConfig.Extension.isDisabled(plugin.id)) {
        disabled.push(plugin.id);
        return;
      }
      register.push(plugin);
    });
  } catch (e) {
    console.error(e);
  }
  try {
    extMod = require('@jupyterlab/terminal-extension/');
    extension = extMod.default;

    // Handle CommonJS exports.
    if (!extMod.hasOwnProperty('__esModule')) {
      extension = extMod;
    }

    plugins = Array.isArray(extension) ? extension : [extension];
    plugins.forEach(function(plugin) {
      if (PageConfig.Extension.isDeferred(plugin.id)) {
        deferred.push(plugin.id);
        ignorePlugins.push(plugin.id);
      }
      if (PageConfig.Extension.isDisabled(plugin.id)) {
        disabled.push(plugin.id);
        return;
      }
      register.push(plugin);
    });
  } catch (e) {
    console.error(e);
  }
  try {
    extMod = require('@jupyterlab/theme-dark-extension/');
    extension = extMod.default;

    // Handle CommonJS exports.
    if (!extMod.hasOwnProperty('__esModule')) {
      extension = extMod;
    }

    plugins = Array.isArray(extension) ? extension : [extension];
    plugins.forEach(function(plugin) {
      if (PageConfig.Extension.isDeferred(plugin.id)) {
        deferred.push(plugin.id);
        ignorePlugins.push(plugin.id);
      }
      if (PageConfig.Extension.isDisabled(plugin.id)) {
        disabled.push(plugin.id);
        return;
      }
      register.push(plugin);
    });
  } catch (e) {
    console.error(e);
  }
  try {
    extMod = require('@jupyterlab/theme-light-extension/');
    extension = extMod.default;

    // Handle CommonJS exports.
    if (!extMod.hasOwnProperty('__esModule')) {
      extension = extMod;
    }

    plugins = Array.isArray(extension) ? extension : [extension];
    plugins.forEach(function(plugin) {
      if (PageConfig.Extension.isDeferred(plugin.id)) {
        deferred.push(plugin.id);
        ignorePlugins.push(plugin.id);
      }
      if (PageConfig.Extension.isDisabled(plugin.id)) {
        disabled.push(plugin.id);
        return;
      }
      register.push(plugin);
    });
  } catch (e) {
    console.error(e);
  }
  try {
    extMod = require('@jupyterlab/tooltip-extension/');
    extension = extMod.default;

    // Handle CommonJS exports.
    if (!extMod.hasOwnProperty('__esModule')) {
      extension = extMod;
    }

    plugins = Array.isArray(extension) ? extension : [extension];
    plugins.forEach(function(plugin) {
      if (PageConfig.Extension.isDeferred(plugin.id)) {
        deferred.push(plugin.id);
        ignorePlugins.push(plugin.id);
      }
      if (PageConfig.Extension.isDisabled(plugin.id)) {
        disabled.push(plugin.id);
        return;
      }
      register.push(plugin);
    });
  } catch (e) {
    console.error(e);
  }
  try {
    extMod = require('@jupyterlab/ui-components-extension/');
    extension = extMod.default;

    // Handle CommonJS exports.
    if (!extMod.hasOwnProperty('__esModule')) {
      extension = extMod;
    }

    plugins = Array.isArray(extension) ? extension : [extension];
    plugins.forEach(function(plugin) {
      if (PageConfig.Extension.isDeferred(plugin.id)) {
        deferred.push(plugin.id);
        ignorePlugins.push(plugin.id);
      }
      if (PageConfig.Extension.isDisabled(plugin.id)) {
        disabled.push(plugin.id);
        return;
      }
      register.push(plugin);
    });
  } catch (e) {
    console.error(e);
  }
  try {
    extMod = require('@jupyterlab/vdom-extension/');
    extension = extMod.default;

    // Handle CommonJS exports.
    if (!extMod.hasOwnProperty('__esModule')) {
      extension = extMod;
    }

    plugins = Array.isArray(extension) ? extension : [extension];
    plugins.forEach(function(plugin) {
      if (PageConfig.Extension.isDeferred(plugin.id)) {
        deferred.push(plugin.id);
        ignorePlugins.push(plugin.id);
      }
      if (PageConfig.Extension.isDisabled(plugin.id)) {
        disabled.push(plugin.id);
        return;
      }
      register.push(plugin);
    });
  } catch (e) {
    console.error(e);
  }
  var lab = new JupyterLab({
    mimeExtensions: mimeExtensions,
    disabled: {
      matches: disabled,
      patterns: PageConfig.Extension.disabled
        .map(function (val) { return val.raw; })
    },
    deferred: {
      matches: deferred,
      patterns: PageConfig.Extension.deferred
        .map(function (val) { return val.raw; })
    },
  });
  register.forEach(function(item) { lab.registerPluginModule(item); });
  lab.start({ ignorePlugins: ignorePlugins });

  // Expose global lab instance when in dev mode.
  if ((PageConfig.getOption('devMode') || '').toLowerCase() === 'true') {
    window.lab = lab;
  }

  // Handle a browser test.
  var browserTest = PageConfig.getOption('browserTest');
  if (browserTest.toLowerCase() === 'true') {
    var el = document.createElement('div');
    el.id = 'browserTest';
    document.body.appendChild(el);
    el.textContent = '[]';
    el.style.display = 'none';
    var errors = [];
    var reported = false;
    var timeout = 25000;

    var report = function() {
      if (reported) {
        return;
      }
      reported = true;
      el.className = 'completed';
    }

    window.onerror = function(msg, url, line, col, error) {
      errors.push(String(error));
      el.textContent = JSON.stringify(errors)
    };
    console.error = function(message) {
      errors.push(String(message));
      el.textContent = JSON.stringify(errors)
    };

    lab.restored
      .then(function() { report(errors); })
      .catch(function(reason) { report([`RestoreError: ${reason.message}`]); });

    // Handle failures to restore after the timeout has elapsed.
    window.setTimeout(function() { report(errors); }, timeout);
  }

}

window.addEventListener('load', main);
