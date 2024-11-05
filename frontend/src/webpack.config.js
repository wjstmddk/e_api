const HtmlWebpackPlugin=require("html-webpack-plugin");

module.exports={
    mode: "develope"
    entry: "./src/index.js"
    output: {
        filename:"bundle.js"
    },
    devServer:{
        host: 'localhost',
        port: 3000,
        open: true,
    },
    module:{
        rules:[
            {
                test:/\.jsx?/,
                loader:'babel-loader',
                options:{
                    presets:['@babel/preset-env','@babel/preset-react']
                }
            },
            {
                test:/\.html?\,
                loader:"html-loader"
                options:{
                    minimize: true,
                }
            }
        ]
    },
    plugins:[
        new HtmlWebpackPlugin({
            template: 'index.html',
        })
    ]
};