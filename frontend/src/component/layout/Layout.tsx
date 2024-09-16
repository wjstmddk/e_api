import React from "react"
import Footer from "./Footer.tsx"
import Header from "./Header.tsx"
const Layout=(props:{
    children: React.ReactNode
})=>{
    return(
        <div>
            <Header/>
            
            <main>
                {props.children}
            </main>
            
            <Footer/>
        </div>
    )
}

export default Layout