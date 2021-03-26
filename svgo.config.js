const { extendDefaultPlugins } = require('svgo');
module.exports = {
  js2svg: {
    pretty: true,
    indent: 2,
  },
  multipass: true,
  plugins: extendDefaultPlugins([
    {
      name: 'addAttributesToSVGElement',
      params: {
        attributes: [
          {
            focusable: false,
          },
          'height',
          'width',
        ],
      },
    },
    {
      name: 'convertColors',
      params: {
        currentColor: 'red',
      },
    },
    {
      name: 'inlineStyles',
      params: {
        onlyMatchedOnce: false,
      },
    },
    {
      name: 'removeAttrs',
      params: {
        attrs: '(baseProfile|class|clip-rule|id|stroke-miterlimit|version)',
      },
    },
    { name: 'removeTitle' },
    {
      name: 'removeViewBox',
      active: false,
    },
    {
      name: 'removeUnknownsAndDefaults',
      params: {
        unknownAttrs: false,
      },
    },
    { name: 'sortAttrs' },
  ]),
};
