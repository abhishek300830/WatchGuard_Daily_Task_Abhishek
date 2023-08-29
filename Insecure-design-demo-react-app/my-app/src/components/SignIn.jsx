import * as React from 'react';
import Avatar from '@mui/material/Avatar';
import Button from '@mui/material/Button';
import CssBaseline from '@mui/material/CssBaseline';
import TextField from '@mui/material/TextField';
import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';
import LockOutlinedIcon from '@mui/icons-material/LockOutlined';
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import { NavLink, useNavigate } from 'react-router-dom';
import json_data from '../data/users.json'

const defaultTheme = createTheme();



export default function SignIn() {
const navigate = useNavigate()

  const handleSubmit = (event) => {
    event.preventDefault();
    const data = new FormData(event.currentTarget);
    let email = data.get('email')
    let pasword = data.get('password')

    let isValidEmail = false
    let isloginAllowed = false
    
    json_data.forEach((user)=>{
        if (user.email === email){
            isValidEmail = true
            if(user.password === pasword){
                isloginAllowed = true
            }else{
                console.log("Wrong password")
            }
        }
    })

    if (!isValidEmail){
        console.log("Please Enter correct Email")
    }

    if (isloginAllowed){
        navigate("/dashboard")
    }
  };


  return (
    <ThemeProvider theme={defaultTheme}>
      <Container component="main" maxWidth="xs">
        <CssBaseline />
        <Box
          sx={{
            marginTop: 8,
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
          }}
        >
          <Avatar sx={{ m: 1, bgcolor: 'secondary.main' }}>
            <LockOutlinedIcon />
          </Avatar>
          <Typography component="h1" variant="h5">
            Sign in
          </Typography>
          <Box component="form" onSubmit={handleSubmit} noValidate sx={{ mt: 1 }}>
            <TextField
              margin="normal"
              required
              fullWidth
              id="email"
              label="Email Address"
              name="email"
              autoComplete="email"
              autoFocus
            />
            <TextField
              margin="normal"
              required
              fullWidth
              name="password"
              label="Password"
              type="password"
              id="password"
              autoComplete="current-password"
            />
            <Button
              type="submit"
              fullWidth
              variant="contained"
              sx={{ mt: 3, mb: 2 }}
            >
              Sign In
            </Button>
            <Grid container>
              <Grid item xs>
                <NavLink to="/forgetpassword" variant="body2" style={{textDecoration:"none"}}>
                  Forgot password?
                </NavLink>
              </Grid>
              <Grid item>
                <NavLink to={"/signup"} variant="body2" style={{textDecoration:"none"}}>
                  {"Don't have an account? Sign Up"}
                </NavLink>
              </Grid>
            </Grid>
          </Box>
        </Box>
      
      </Container>
    </ThemeProvider>
  );
}