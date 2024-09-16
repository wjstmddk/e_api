import React from "react"
import { Link } from "react-router-dom"

const Header=()=>{
    return(
        <><header>
            <div>header</div>
        </header>
            <nav>
                <ul>
                    <li>
                        <Link to="/">홈</Link>
                    </li>
                    <li>
                        <Link to="/test">메뉴2</Link>
                    </li>
                    <li>
                        <Link to="/testinput">메뉴3</Link>
                    </li>
                </ul>
            </nav></>
    )
}

export default Header