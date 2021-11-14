<template>
  <div>
    <Nav></Nav>
    <div class="w-100 bg-light">
      <v-card @click="createSurvey(originFormData)" class="d-inline-block m-5" style="width:150px;">
        <v-container class="d-flex justify-content-center">
          <v-icon x-large>mdi-plus</v-icon>
        </v-container>
      </v-card>

      <!-- <button @click="goCreateSurvey()">설문지 작성</button> -->
    </div>

    <div class="main">
      <div class="new-container">
        <p>내가 작성한 설문지</p>
        <div class="row">
          <v-card
            @click="fetchEditForm(survey) + fetchStudentResponse(survey.pk)"
            v-for="survey in surveys"
            :key="`survey_${survey.pk}`"
            class="m-3"
            width="250px"
            height="320px"
            style="cursor: pointer;"
          >
            <v-img v-if="survey.color === '#FFCDD2'" class="white--text align-end" height="200px" width="100%" src="../../assets/red.jpg"> </v-img>
            <v-img v-if="survey.color === '#F8BBD0'" class="white--text align-end" height="200px" src="../../assets/pink.jpg"> </v-img>
            <v-img v-else-if="survey.color === '#F3E5F5'" class="white--text align-end" height="200px" src="../../assets/purple.jpg"> </v-img>
            <v-img v-if="survey.color === '#D1C4E9'" class="white--text align-end" height="200px" src="../../assets/deep-purple.jpg"> </v-img>
            <v-img v-if="survey.color === '#C5CAE9'" class="white--text align-end" height="200px" src="../../assets/indigo.jpg"> </v-img>
            <v-img v-if="survey.color === '#BBDEFB'" class="white--text align-end" height="200px" src="../../assets/blue.jpg"> </v-img>
            <v-img v-if="survey.color === '#B3E5FC'" class="white--text align-end" height="200px" src="../../assets/light-blue.jpg"> </v-img>
            <v-img v-if="survey.color === '#B2EBF2'" class="white--text align-end" height="200px" src="../../assets/cyan.jpg"> </v-img>
            <v-img v-if="survey.color === '#B2DFDB'" class="white--text align-end" height="200px" src="../../assets/teal.jpg"> </v-img>
            <v-img v-if="survey.color === '#C8E6C9'" class="white--text align-end" height="200px" src="../../assets/green.jpg"> </v-img>
            <v-img v-if="survey.color === '#DCEDC8'" class="white--text align-end" height="200px" src="../../assets/light-green.jpg"> </v-img>
            <v-img v-if="survey.color === '#F0F4C3'" class="white--text align-end" height="200px" src="../../assets/lime.jpg"> </v-img>
            <v-img v-if="survey.color === '#FFF9C4'" class="white--text align-end" height="200px" src="../../assets/yellow.jpg"> </v-img>
            <v-img v-if="survey.color === '#FFECB3'" class="white--text align-end" height="200px" src="../../assets/amber.jpg"> </v-img>
            <v-img v-if="survey.color === '#FFE0B2'" class="white--text align-end" height="200px" src="../../assets/orange.jpg"> </v-img>
            <v-img v-if="survey.color === '#FFCCBC'" class="white--text align-end" height="200px" src="../../assets/deep-orange.jpg"> </v-img>
            <v-img v-if="survey.color === '#D7CCC8'" class="white--text align-end" height="200px" src="../../assets/brown.jpg"> </v-img>
            <v-img v-if="survey.color === '#CFD8DC'" class="white--text align-end" height="200px" src="../../assets/blue-grey.jpg"> </v-img>
            <v-img v-if="survey.color === '#F5F5F5'" class="white--text align-end" height="200px" src="../../assets/grey.jpg"> </v-img>
            <v-card-text class="text--primary text-left">
              {{ survey.title }}
            </v-card-text>
            <v-card-text class="text-left">
              {{ survey.created_at }}
            </v-card-text>
          </v-card>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Nav from "@/components/Nav.vue";
import { mapState, mapActions } from "vuex";

export default {
  components: {
    Nav,
  },
  computed: {
    ...mapState(["surveys", "originFormData"]),
  },
  methods: {
    ...mapActions(["fetchSurveys", "fetchEditForm", "createSurvey", "fetchResultForm", "fetchStudentResponse"]),
  },
  created() {
    this.fetchSurveys();
    console.log(false * 100);
  },
};
</script>

<style>
.main {
  margin: 30px 80px;
}
</style>
