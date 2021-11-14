<template>
  <div style="margin: 0;" class='bg'>
    <Nav></Nav>
    <div class="text-center">
      <img src="@/assets/빨간.jpg" width=32%>
    </div>
    <div class="d-flex justify-content-center">
      <v-container class="d-flex  mt-0 pt-0">
        <v-layout column class="p-3 w-50">
          <v-card-title class="m-0 p-0">Students: {{ $store.getters.studentsCount }}</v-card-title>
          <Students></Students>
        </v-layout>
        <v-layout column class="p-1 w-50">
          <v-card-title class="m-2 p-0">Register</v-card-title>
          <Register></Register>
        </v-layout>
      </v-container>
    </div>
  </div>
</template>

<script>
import Students from "@/components/Student/Students.vue";
import Register from "@/components/Student/Register.vue";
import Nav from "@/components/Nav.vue"

export default {
  components: {
    Students,
    Register,
    Nav,
  },
  data() {
    return {};
  },
  methods: {},
  mounted() {
    this.$store.state.Students = [];
    this.$store.dispatch("getStudents");
  },
};
</script>

<style scoped>
div {
  margin: 5px;
}

.title_font{
  font-family: 'Jua', sans-serif;
}
</style>
