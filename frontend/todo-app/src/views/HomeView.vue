<script setup>
</script>

<template>
  <div class="col-md-6 mx-auto mt-5">
    <div class="form-group d-flex">
      <input type="text" class="form-control" placeholder="Enter Todo Name" v-model="todo">
      <button class="btn btn-success" @click="createTodo()">Create</button>
    </div>
    <ul class="list-group mt-4">
      <li class="list-group-item d-flex justify-content-between" v-for="todo in todos" :key="todo.uid">
        <s style="max-width:40%" class="px-1" v-if="todo.is_completed">{{todo.todo_name}}</s>
        <div style="margin-bottom: 0;" v-else>{{todo.todo_name}}</div>
        <div>
          <button class="btn btn-success" @click="updateTodo(todo.uid, todo.is_completed)">Toggle Status</button>
          <button class="btn btn-danger align-self-end mx-2" @click="deleteTodo(todo.uid)">Delete</button>
        </div>
      </li>
    </ul>
  </div>
  
</template>


<script>

export default {
  name: "HomeView",
  components: {
    
  },
  data(){
    return {
      todo: '',
      todos: [],
    }
  },
  
  created(){
    this.getTodos();
  },

  methods: {
    createTodo(){
      const token = localStorage.getItem('token');
      const requestOptions = {
          method: 'POST',
          headers: { 'Content-Type': 'application/json', 'Access-Control-Allow-Origin': 'http://localhost:5173', 'Access-Control-Allow-Credentials': 'true', 'Authorization': `Bearer ${token}` },
          body: JSON.stringify({ todo_name: this.todo}),
        };

        try{
        fetch('http://localhost:8000/api/todo/add', requestOptions)
          .then(response => response.json())
          .then(data => {
            console.log("data", data);
            this.getTodos();
        });}
        catch(err){
          console.log(err);
        }
    },
    getTodos(){
      const token = localStorage.getItem('token');
      const requestOptions = {
          method: 'GET',
          headers: { 'Content-Type': 'application/json', 'Access-Control-Allow-Origin': 'http://localhost:5173', 'Access-Control-Allow-Credentials': 'true', 'Authorization': `Bearer ${token}` },
        };

        try{
        fetch('http://localhost:8000/api/todo/view', requestOptions)
          .then(response => response.json())
          .then(data => {
            this.todos = data.data;
        });}
        catch(err){
          console.log(err);
        }
    },
    updateTodo(uid, is_completed){
      const token = localStorage.getItem('token');
      const requestOptions = {
          method: 'PATCH',
          headers: { 'Content-Type': 'application/json', 'Access-Control-Allow-Origin': 'http://localhost:5173', 'Access-Control-Allow-Credentials': 'true', 'Authorization': `Bearer ${token}` },
          body: JSON.stringify({ uid: uid, is_completed: !is_completed}),
        };

        try{
        fetch('http://localhost:8000/api/todo/update', requestOptions)
          .then(response => response.json())
          .then(data => {
            console.log("data", data);
            this.getTodos();
        });}
        catch(err){
          console.log(err);
        }
    },
    deleteTodo(uid){
      const token = localStorage.getItem('token');
      const requestOptions = {
          method: 'DELETE',
          headers: { 'Content-Type': 'application/json', 'Access-Control-Allow-Origin': 'http://localhost:5173', 'Access-Control-Allow-Credentials': 'true', 'Authorization': `Bearer ${token}` },
          body: JSON.stringify({ uid: uid}),
        };

        try{
        fetch('http://localhost:8000/api/todo/delete', requestOptions)
          .then(response => response.json())
          .then(() => {
            this.getTodos();
        });}
        catch(err){
          console.log(err);
        }
    }

  }
}
</script>