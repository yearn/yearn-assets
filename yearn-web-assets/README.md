# yearn-web-assets

[![JavaScript Style Guide](https://img.shields.io/badge/code_style-standard-brightgreen.svg)](https://standardjs.com)

Tokens assets for the Yearns web projects.
## Install
This package is handled by Github's system. In order to be able to install it, first add the following to your `.npmrc` or `.yarnrc` file:
```
# For .npmrc
@yearn:registry=https://npm.pkg.github.com
```

```
# For .yarnrc
registry=https://npm.pkg.github.com/yearn
```

Then you can install is as usual:
```bash
yarn add @yearn/yearn-web-assets
```

## Usage

```jsx
import React, { Component, useState } from 'react'
import Token from 'yearn-web-tokens'

class Example extends Component {
  render() {
    return (
      <Token
        format={'svg'} //svg or img
        address={'0xFd086bC7CD5C481DCC9C85ebE478A1C0b69FCbb9'} // token address, checksummed
        chainID={'42161'} // chain id
        imgSize={'32'} // only if format is img, default is 128, can be 32 or 128
      />
    )
  }
}
```
