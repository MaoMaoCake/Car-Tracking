import React from "react";
import PropTypes from "prop-types";
import List from "@material-ui/core/List";
import ListItem from "@material-ui/core/ListItem";
import ListItemText from "@material-ui/core/ListItemText";
import Collapse from "@material-ui/core/Collapse";
import { Typography, Box, Grid } from '@material-ui/core';
import ExpandLess from "@material-ui/icons/ExpandLess";
import ExpandMore from "@material-ui/icons/ExpandMore";
import Divider from "@material-ui/core/Divider";
import { withStyles } from "@material-ui/styles";
import {getCookie} from "./cookie";
import {Link} from "react-router-dom";
import Button from '@material-ui/core/Button';
import { styled } from "@material-ui/styles";
import Stack from "@material-ui/core/Stack";
import ReactDOM from "react-dom";

import GT from "./GT";
import drawMap from "./map";
import Logout from "./Logout";

const styles = theme => ({
    root: {
        width: "150%",
        maxWidth: 360,
        text: "text.primary",
        //background: theme.palette.background.paper
    },
    nested: {
        // paddingLeft: theme.spacing(4)
    }
});

class NestedList extends React.Component {
    state = {};
    handleClick = e => {
        this.setState({ [e]: !this.state[e] });
    };
    render() {
        const items = GT(getCookie("token"));
        const { classes } = this.props;
        let Name = getCookie("username");
        const BootstrapButton = styled(Button)({
            boxShadow: "true",
            textTransform: "none",
            fontSize: 16,
            padding: "1px 20px",
            border: "1px solid",
            lineHeight: 1.5,
            backgroundColor: "#808080",
            borderColor: "#808080"
          });
        if (Name !== ""){
            return (
                <div>
                    <Box sx={{ width: '150%', maxWidth: 300, my: 3, mx: 3 }}>
                        <Grid container alignItems="center">
                            <Grid item xs>
                                <Typography gutterBottom variant="h5" component="div">
                                    Hello {Name}
                                </Typography>
                            </Grid>
                        </Grid>
                    </Box>
                    <Divider variant="middle" />
                    {items.list.map(list => {
                        return (
                            <List
                                className={classes.root}
                                key={list.id}
                            >
                                
                                {list.items.map(item => {
                                    return (
                                        <div key={item.id}>
                                            {item.subitems != null ? (
                                                <div key={item.id}>
                                                    <ListItem
                                                        button
                                                        key={item.id}
                                                        onClick={this.handleClick.bind(
                                                            this,
                                                            item.name
                                                        )}
                                                    >
                                                        <ListItemText
                                                            primary={item.name}
                                                        />
                                                        {this.state[item.name] ? (
                                                            <ExpandLess />
                                                        ) : (
                                                            <ExpandMore />
                                                        )}
                                                    </ListItem>
                                                    <Collapse
                                                        key={list.items.id}
                                                        component="li"
                                                        in={this.state[item.name]}
                                                        timeout="auto"
                                                        unmountOnExit
                                                    >
                                                        <List disablePadding>
                                                            {item.subitems.map(
                                                                sitem => {
                                                                    return (
                                                                        <ListItem
                                                                            button
                                                                            key={
                                                                                sitem.id
                                                                            }
                                                                            className={
                                                                                classes.nested
                                                                            }
                                                                            onClick={function (){
                                                                                document.getElementById("device_name").innerText = sitem.name
                                                                                // mapping api here
                                                                                ReactDOM.render(drawMap(sitem.id), document.getElementById('Map'))
                                                                            }}
                                                                            style={{"color":sitem.color}}
                                                                        > {/* ^map the function to individual buttons*/}
                                                                            <ListItemText
                                                                                key={
                                                                                    sitem.id
                                                                                }
                                                                                primary={
                                                                                    sitem.name
                                                                                }
                                                                            />
                                                                        </ListItem>
                                                                    );
                                                                }
                                                            )}
                                                        </List>
                                                    </Collapse>{" "}
                                                </div>
                                            ) : (
                                                <ListItem
                                                    button
                                                    onClick={this.handleClick.bind(
                                                        this,
                                                        item.name
                                                    )}
                                                    key={item.id}
                                                >
                                                    <ListItemText
                                                        primary={item.name}
                                                    />
                                                </ListItem>
                                            )}
                                        </div>
                                    );
                                })}
                                <Divider key={list.id} absolute />
                            </List>
                        );
                        
                    })}
                    <Stack spacing={2} direction="row" marginY = {45} marginX = {-1}>
                        <BootstrapButton variant="contained" onClick={Logout}>Log out</BootstrapButton>
                    </Stack>
                </div>
            );
        }
    else{
        return (
            <h2>Please <Link to="/login">Login</Link></h2>
        );
    }
    }
}
NestedList.propTypes = {
    classes: PropTypes.object.isRequired
};
// export default withStyles(styles)(NestedList);
export const NavBarNL = withStyles(styles)(NestedList);