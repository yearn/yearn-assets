import React, { Suspense } from 'react';

const Fallback = ({width = 32, height = 32}) => {
	return (
		<div style={{
			borderRadius: 99999,
			width: width - 2,
			height: height - 2,
			background: '#F9FBFD',
			border: '1px solid #E0EAFF'
		}} />
	)
}
const Token = ({chainID, address, format = 'svg', imgSize = '128', width = 32, height = 32, ...props}) => {
	if (format === 'img' && imgSize === '32') {
		const TokenAsReact = React.lazy(() => 
			import(`./tokens/${chainID}/${address}/TokenImage32.js`)
			.catch(() => console.error(`Impossible to load token ${address}`))
		);

		return (
			<Suspense fallback={<Fallback width={width} height={height} />}>
				<TokenAsReact width={width} height={height} {...props} />
			</Suspense>
		);
	}

	if (format === 'img' && imgSize === '128') {
		const TokenAsReact = React.lazy(() => 
			import(`./tokens/${chainID}/${address}/TokenImage128.js`)
			.catch(() => console.error(`Impossible to load token ${address}`))
		);

		return (
			<Suspense fallback={<Fallback width={width} height={height} />}>
				<TokenAsReact width={width} height={height} {...props} />
			</Suspense>
		);
	}

	const TokenAsReact = React.lazy(() => 
		import(`./tokens/${chainID}/${address}/TokenSVG.js`)
		.catch(() => console.error(`Impossible to load token ${address}`))
	);

	return (
		<Suspense fallback={<Fallback width={width} height={height} />}>
			<TokenAsReact width={width} height={height} {...props} />
		</Suspense>
	);
}
export default Token;
