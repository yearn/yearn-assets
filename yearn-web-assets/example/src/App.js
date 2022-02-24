import React from 'react'
import Token from 'yearn-web-tokens'

const App = () => {
  return (
    <div>
      <Token
        format={'svg'}
        address={'0xFd086bC7CD5C481DCC9C85ebE478A1C0b69FCbb9'}
        onClick={() => alert(`Hello Web3`)}
        style={{cursor: 'pointer'}}
        chainID={'42161'} />
      <Token
        format={'svg'}
        address={'0x0d4EA8536F9A13e4FBa16042a46c30f092b06aA5'}
        width={48}
        height={48}
        chainID={'1'} />
        <Token
        format={'img'}
        address={'0x1AEf73d49Dedc4b1778d0706583995958Dc862e6'}
        chainID={'1'}
        imgSize={'32'} />
        <Token
        format={'img'}
        address={'0x0FCDAeDFb8A7DfDa2e9838564c5A1665d856AFDF'}
        width={48}
        height={48}
        chainID={'250'} />
      </div>
  );
}

export default App
