import React, { Suspense } from 'react';

const Token = ({ chainID, address, format = 'svg', imgSize = '128'}) => {
	if (format === 'img' && imgSize === '32') {
		const TokenAsReact = React.lazy(() => import(`./tokens/${chainID}/${address}/TokenImage32.js`));
		return (
			<Suspense fallback={<div style={{borderRadius: 99999, width: 32, height: 32, background: '#F9FBFD', border: '1px solid #E0EAFF'}} />}>
				<TokenAsReact />
			</Suspense>
		);
	}
	if (format === 'img' && imgSize === '128') {
		const TokenAsReact = React.lazy(() => import(`./tokens/${chainID}/${address}/TokenImage128.js`));
		return (
			<Suspense fallback={<div style={{borderRadius: 99999, width: 128, height: 128, background: '#F9FBFD', border: '1px solid #E0EAFF'}} />}>
				<TokenAsReact />
			</Suspense>
		);
	}
	const TokenAsReact = React.lazy(() => import(`./tokens/${chainID}/${address}/TokenSVG.js`));
	return (
		<Suspense fallback={<div style={{borderRadius: 99999, width: 32, height: 32, background: '#F9FBFD', border: '1px solid #E0EAFF'}} />}>
			<TokenAsReact />
		</Suspense>
	);
}
export default Token;
