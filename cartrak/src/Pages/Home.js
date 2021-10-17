import NavBar from "../Component/Nav";
import MView from "../Component/MView";
import { NavBarNL } from "../Component/NavBarNL";

export default function Home(){
    return (
        <div id="app">
            {/* <NavBar /> */}
            <NavBarNL/>
            <MView />
        </div>
    )
}
