<template>
  <div class="h-100">
    <div class="bg h-100">
      <div class="d-flex flex-column align-items-center">
        <v-card class="mybtn" :color="mycolor" @click="fetchResponseForm([$route.query.name, $route.query.s_pk, $route.query.s_num]) + fetchStudentResponse($route.query.s_pk) + fetchStudent($route.query.s_num)" style="margin-top: 20vh;">
          <v-container class="d-flex flex-column justify-content-center align-items-center">
            <h2>설문 시작하기</h2>
            <v-icon x-large class="fas fa-edit mb-5"></v-icon>
            <p class="text-center">
              오시느라 수고하셨습니다
              <br />아침 설문 부탁해요!
            </p>
          </v-container> 
        </v-card>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  data() {
    return {
      mycolor: "rgba(255,255,255,0.5)",
    };
  },
  methods: {
    ...mapActions(['fetchResponseForm', 'fetchStudentResponse', 'fetchStudent']),
  },
}
</script>

<style scoped>
.bg {
  background-image: url("../../assets/p9.jpg");
  background-size: cover;
}
.mybtn {
  width: 300px;
  height: 300px;
  cursor: pointer;
}
</style>