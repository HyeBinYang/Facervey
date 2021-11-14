<template>
  <div class="h-100">
    <div class="bg h-100">
        <img src="@/assets/노란.jpg" class='m-4' width=15%>
      <div class="d-flex flex-column align-items-center">
        <div class="d-flex justify-content-center align-items-center">
          <div
            style="background-color: rgba(255,255,255,0.8);border-radius: 25px;"
            class="mybtn m-5 p-5"
          >
            <div class="d-flex flex-column justify-content-center align-items-center">
              <v-icon x-large>mdi-bookmark</v-icon>
              <h2 class="m-3 myfont">학생</h2>

              <div class="btn btn-primary w-50" @click="move('Student')">등록</div>
            </div>
          </div>

          <div
            style="background-color: rgba(255,255,255,0.8); border-radius: 25px;"
            class="mybtn m-5 p-5"
            
          >
            <div class="d-flex flex-column justify-content-center align-items-center">
              <v-icon x-large>mdi-clipboard-edit</v-icon>
              <h2 class="m-3 myfont">설문</h2>
              <div class="btn btn-primary w-50" @click="goSurveyList">작성</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      mycolor: "rgba(255,255,255,0.5)",
    };
  },
  methods: {
    move(val) {
      this.$router.push({ name: val });
    },
    goSurveyList() {
      this.$router.push({ name: 'SurveyList' })
    },
  },

};
</script>

<style scoped>
.bg {
  background-image: url("../assets/p9.jpg");
  background-size: cover;
}
.mybtn {
  width: 250px;
  height: 250px;
}

.myhover :hover {
  background-color: white;
}

.myfont {
  font-family: "Noto Serif KR", serif;
}
</style>