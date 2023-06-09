<template>
  <div class="login">
    <div class="container d-flex flex-column" style="margin-top: 4em; align-items: center;; max-width: 500px;">
      <h1 style="color: hsla(160, 100%, 37%, 1)">Sign In</h1>
      <form class="p-3" style="margin: 2em; border-radius: 10px; border: 3px solid hsla(160, 100%, 37%, 1)">
        <div class="mb-3 d-flex flex-column align-items-center mx-auto my-md-4" style="width: 300px">
          <label for="exampleInputUsername" class="form-label" style="color: hsla(160, 100%, 37%, 1); font-size: large;">Username</label>
          <input type="text" v-model="username" class="form-control mt-2 mb-3" id="exampleInputUsername">
        </div>
        <div class="mb-3 d-flex flex-column align-items-center mx-auto" style="width: 300px;">
          <label for="exampleInputPassword1" class="form-label" style="color:hsla(160, 100%, 37%, 1); font-size: large;">Password</label>
          <input type="password" v-model="password" class="form-control mt-3" id="exampleInputPassword1">
        </div>
        <button type="submit" @click="onSubmit" class="btn btn-primary" style="background-color: hsla(160, 100%, 37%, 1); color: black; font-weight: bold; margin: 2em auto; padding: 0.7em 7.6em;">Submit</button>
      </form>
    </div>
  </div>
</template>



<script>
  export default {
    data() {
      return {
        username: '',
        password: '',
      }
    },
    methods:{
      onSubmit(e){
        e.preventDefault();

        if(!this.username.length)
          alert("Username is required");
        else if(!this.password.length)
          alert("Password is required");
        
        const requestOptions = {
          method: 'POST',
          headers: { 'Content-Type': 'application/json', 'Access-Control-Allow-Origin': 'http://localhost:5173', 'Access-Control-Allow-Credentials': 'true' },
          body: JSON.stringify({ username: this.username, password: this.password }),
        };

        try{
        fetch('http://localhost:8000/api/token/', requestOptions)
          .then(response => response.json())
          .then(data => {
            console.log("data", data);
            localStorage.setItem('token', data.access);
            localStorage.setItem('refresh_token', data.refresh);
            window.location.href = '/';

        });}
        catch(err){
          console.log(err);
        }
      },
    }
  }
</script>