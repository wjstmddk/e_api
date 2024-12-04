const HtmlWebpackPlugin=require("html-webpack-plugin");
const ReactRefreshWebpackPlugin = require('@pmmmwh/react-refresh-webpack-plugin');

module.exports={
    mode: "development",
    entry: "./src/index.js",
    output: {
        filename:"bundle.js"
    },
    devServer:{
        host: '0.0.0.0',
        port: 3000,
        open: true,
    },
    module:{
        rules:[
            {
                test:/\.jsx?/,
                loader:'babel-loader',
                options:{
                    presets:['@babel/preset-env','@babel/preset-react'],
                    plugins:['react-refresh/babel']
                }
            },
            {
                test:/\.html$/,
                loader:"html-loader",
                options:{
                    minimize: true
                }
            }, {
                test: /\.css$/, // CSS 파일 처리
                use: ["style-loader", "css-loader"], // 처리에 필요한 loader들
            },
            {
                test:/\.tsx?$/, // .ts와 .tsx 파일 처리
                loader: 'babel-loader',
                exclude: /node_modules/,
                options: {
                    presets: [
                        '@babel/preset-env',
                        '@babel/preset-react',
                        '@babel/preset-typescript', // TypeScript 지원 추가
                    ],
                },
            }
        ]
    },
    resolve:{
        extensions: [".js", ".jsx",".ts",".tsx"]
    },
    plugins: [
        new ReactRefreshWebpackPlugin(),
        new HtmlWebpackPlugin({
            template: './public/index.html',
        })
    ]
};