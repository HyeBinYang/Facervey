<template>
  <div style="height: 100%">
    <Nav></Nav>
    <v-tabs
      fixed-tabs
      v-model="tab"
    >
      <v-tab 
        v-for="item in items"
        :key="item"
      >
          {{ item }}
      </v-tab>
    </v-tabs>
    <v-tabs-items v-model="tab" style="height: 100%;">
      <v-tab-item
        v-for="item in items"
        :key="item"
        style="height: 100%;"
      >
        <div v-if="item === '설문'" :style="{ background: FormData.survey.color }" style="height: 100%; padding-top: 50px; padding-bottom: 50px;">
          <v-card style="position: fixed; bottom: 40%; right: 9vw; border-radius: 12px;">
            <div class="my-5 mx-3 text-center">
              <v-icon @click="createQuestion(questionForm) + addQuestion()" class="fas fa-plus-circle"></v-icon>
            </div>
            <div>
              <v-row justify="center">
                <v-dialog v-model="dialog" scrollable max-width="600px">
                  <template v-slot:activator="{ on, attrs }">
                    <div class="mb-5 text-center">
                      <v-icon v-bind="attrs" v-on="on" class="fas fa-palette"></v-icon>
                    </div>
                  </template>
                  <v-card>
                    <v-card-title class="d-flex">
                      <div class="mr-auto">
                        테마 옵션
                      </div>
                      <v-icon @click="closeModal()" class="fas fa-times"></v-icon>
                    </v-card-title>
                    <div class="mt-5" style="height: 300px;">
                      <v-btn :title="colors[0]" @click="editSurvey(FormData) + setColor()" fab color="red" class="mx-2 mb-2"></v-btn>
                      <v-btn :title="colors[1]" @click="editSurvey(FormData) + setColor()" fab color="pink" class="mx-2 mb-2"></v-btn>
                      <v-btn :title="colors[2]" @click="editSurvey(FormData) + setColor()" fab color="deep-purple" class="mx-2 mb-2"></v-btn>
                      <v-btn :title="colors[3]" @click="editSurvey(FormData) + setColor()" fab color="indigo" class="mx-2 mb-2"></v-btn>
                      <v-btn :title="colors[4]" @click="editSurvey(FormData) + setColor()" fab color="purple" class="mx-2 mb-2"></v-btn>
                      <v-btn :title="colors[5]" @click="editSurvey(FormData) + setColor()" fab color="blue" class="mx-2 mb-2"></v-btn>
                      <v-btn :title="colors[6]" @click="editSurvey(FormData) + setColor()" fab color="light-blue" class="mx-2 mb-2"></v-btn>
                      <v-btn :title="colors[7]" @click="editSurvey(FormData) + setColor()" fab color="cyan" class="mx-2 mb-2"></v-btn>
                      <v-btn :title="colors[8]" @click="editSurvey(FormData) + setColor()" fab color="teal" class="mx-2 mb-2"></v-btn>
                      <v-btn :title="colors[9]" @click="editSurvey(FormData) + setColor()" fab color="green" class="mx-2 mb-2"></v-btn>
                      <v-btn :title="colors[10]" @click="editSurvey(FormData) + setColor()" fab color="light-green" class="mx-2 mb-2"></v-btn>
                      <v-btn :title="colors[11]" @click="editSurvey(FormData) + setColor()" fab color="lime" class="mx-2 mb-2"></v-btn>
                      <v-btn :title="colors[12]" @click="editSurvey(FormData) + setColor()" fab color="yellow" class="mx-2 mb-2"></v-btn>
                      <v-btn :title="colors[13]" @click="editSurvey(FormData) + setColor()" fab color="amber" class="mx-2 mb-2"></v-btn>
                      <v-btn :title="colors[14]" @click="editSurvey(FormData) + setColor()" fab color="orange" class="mx-2 mb-2"></v-btn>
                      <v-btn :title="colors[15]" @click="editSurvey(FormData) + setColor()" fab color="deep-orange" class="mx-2 mb-2"></v-btn>
                      <v-btn :title="colors[16]" @click="editSurvey(FormData) + setColor()" fab color="brown" class="mx-2 mb-2"></v-btn>
                      <v-btn :title="colors[17]" @click="editSurvey(FormData) + setColor()" fab color="blue-grey" class="mx-2 mb-2"></v-btn>
                      <v-btn :title="colors[18]" @click="editSurvey(FormData) + setColor()" fab color="grey" class="mx-2 mb-2"></v-btn>
                    </div>
                  </v-card>
                </v-dialog>
              </v-row>
            </div>
            <div class="mb-5 text-center">
              <v-icon @click="deleteSurvey(FormData)" class="fas fa-trash-alt"></v-icon>
            </div>
          </v-card>
          <v-card style="margin-left: 20vw; margin-right: 20vw; border-radius: 12px;">
            <div style="margin-left: 2vw; margin-right: 2vw; padding-top: 20px">
              <v-text-field
                v-model="FormData.survey.title"
                @keyup="editSurvey(FormData)"
                label="title"
              ></v-text-field>
            </div>
            <div style="margin-left: 2vw; margin-right: 2vw;">
              <v-text-field
                v-model="FormData.survey.description"
                @keyup="editSurvey(FormData)"
                label="description"
              ></v-text-field>
            </div>
          </v-card>
          <v-card v-for="question in FormData.questions" :key="question.pk" style="margin-left: 20vw; margin-right: 20vw; margin-top: 50px; padding-bottom: 20px; border-radius: 12px;">
            <div class="row" style="margin-left: 1vw; margin-right: 1vw;">
              <div class="col-8 pb-0">
                <v-text-field
                  v-model="question.content"
                  @keyup="editSurvey(FormData)"
                  label="질문"
                ></v-text-field>
              </div>
              <div class="col-4">
                <v-overflow-btn
                  class="my-2"
                  v-model="question.q_type"
                  :items="dropdown_font"
                  label="답변 유형"
                ></v-overflow-btn>
              </div>
            </div>
            <div>
              <div v-for="answer in FormData.answers" :key="answer.pk">
                <div v-if="answer.q_pk === question.pk" class="row" style="margin-left: 1vw;">
                  <v-text-field
                    v-model="answer.content"
                    @keyup="editSurvey(FormData)"
                    label="옵션"
                    solo
                  ></v-text-field>
                  <div class="col-2 py-2">
                    <v-btn icon>
                      <v-icon :title="answer.pk" @click="deleteOption(answer) + popOption(answer.pk)" class="fas fa-times delete-opbtn"></v-icon>
                    </v-btn>
                  </div>
                </div>
              </div>
              <div v-if="question.q_type === '객관식'" class="py-0" style="margin-left: 1.5vw;">
                <span @click="createOption([answerForm, question.pk]) + addOption(question.pk)" class="text-primary" style="cursor: pointer;">옵션 추가</span>
              </div>
              <div v-else class="col-4 py-0" style="margin-left: 1.1vw;">
                서술형
              </div>
            </div>
            <hr>
            <div class="d-flex justify-content-end">
              <div class="mr-5">
                <v-btn icon>
                  <v-icon :title="question.pk" @click="deleteQuestion(question) + popQuestion(question.pk)" class="fas fa-trash-alt"></v-icon>
                </v-btn>
              </div>
            </div>
          </v-card>
        </div>
        <div v-else :style="{ background: FormData.survey.color }" style="height: 100%; padding-top: 50px; padding-bottom: 50px;">
          <v-card style="margin-left: 20vw; margin-right: 20vw; border-radius: 12px;">
            <div style="height: 150px; margin-left: 2vw; margin-right: 2vw; padding-top: 20px">
              <h2>응답 0개</h2>
            </div>
          </v-card>
          <v-card style="margin-top: 20px; margin-left: 20vw; margin-right: 20vw; border-radius: 12px;">
            <div style="display: flex; justify-content: center; align-items: center; height: 80px; margin-left: 2vw; margin-right: 2vw; padding-top: 20px">
              <p>응답을 기다리는중...</p>
            </div>
          </v-card>
        </div>
      </v-tab-item>
    </v-tabs-items>
  </div>
</template>

<script>
import Nav from '@/components/Nav.vue'
import { mapActions, mapState } from 'vuex'

export default {
  components: {
    Nav,
  },
  mounted() {
    this.FormData = this.originFormData
    this.FormData.survey.color = '#FFCDD2'
    this.questionForm.surveyss.push(this.originFormData.survey.pk)
    this.answerForm.s_pk = this.originFormData.survey.pk
  },
  data() {
    return {
      colors: [
               'red', 'pink', 'deep-purple', 
               'indigo', 'purple', 'blue', 
               'light-blue', 'cyan', 'teal', 
               'green', 'light-green', 'lime',
               'yellow', 'amber', 'orange',
               'deep-orange', 'brown', 'blue-grey',
               'grey', 
      ],
      originColor: '#FFCDD2',
      activeColor: '#FFCDD2',
      dialogm1: '',
      dialog: false,
      tab: null,
      items: ['설문', '응답'],
      FormData: {
        answers: [],
        questions: [], 
        survey: {
          pk: null,
          title: 'title',
          description: 'description',
          color: null,
          user: {
            pk: null,
            username: null
          }
        },
      },
      dropdown_font: ['객관식', '서술형'],
      questionForm: {
        pk: null,
        q_type: '객관식',
        is_saved: 0,
        content: null,
        surveyss: []
      },
      answerForm: {
        pk: null,
        s_pk: null,
        q_pk: null,
        content: null,
      }
    }
  },
  methods: {
    ...mapActions(['saveSurvey', 'editSurvey', 'deleteSurvey', 'createQuestion', 'createOption', 'deleteQuestion', 'deleteOption']),
    addQuestion() {
      this.FormData.questions.push({
        pk: null,
        q_type: '객관식',
        is_saved: 0,
        content: null,
        surveyss: [this.FormData.survey.pk]
      })
    },
    addOption(pk) {
      this.FormData.answers.push({
        pk: null,
        s_pk: this.FormData.survey.pk,
        q_pk: pk,
        content: null,
      })
    },
    popQuestion(pk) {
      const findItem = this.FormData.questions.find(function (item) {
        return item.pk === pk;
      });
      const idx = this.FormData.questions.indexOf(findItem);
      this.FormData.questions.splice(idx, 1);
    },
    popOption(pk) {
      const findItem = this.FormData.answers.find(function (item) {
        return item.pk === pk;
      });
      const idx = this.FormData.answers.indexOf(findItem);
      this.FormData.answers.splice(idx, 1);
    },
    setColor() {
      const color = event.target.title
      if (color === 'red') {
        this.activeColor = '#FFCDD2'
        this.FormData.survey.color = '#FFCDD2'
      } else if (color === 'purple') {
        this.activeColor = '#F3E5F5'
        this.FormData.survey.color = '#F3E5F5'
      } else if (color === 'blue') {
        this.activeColor = '#BBDEFB'
        this.FormData.survey.color = '#BBDEFB'
      } else if (color === 'pink') {
        this.activeColor = '#F8BBD0'
        this.FormData.survey.color = '#F8BBD0'
      } else if (color === 'deep-purple') {
        this.activeColor = '#D1C4E9'
        this.FormData.survey.color = '#D1C4E9'
      } else if (color === 'indigo') {
        this.activeColor = '#C5CAE9'
        this.FormData.survey.color = '#C5CAE9'
      } else if (color === 'light-blue') {
        this.activeColor = '#B3E5FC'
        this.FormData.survey.color = '#B3E5FC'
      } else if (color === 'cyan') {
        this.activeColor = '#B2EBF2'
        this.FormData.survey.color = '#B2EBF2'
      } else if (color === 'teal') {
        this.activeColor = '#B2DFDB'
        this.FormData.survey.color = '#B2DFDB'
      } else if (color === 'green') {
        this.activeColor = '#C8E6C9'
        this.FormData.survey.color = '#C8E6C9'
      } else if (color === 'light-green') {
        this.activeColor = '#DCEDC8'
        this.FormData.survey.color = '#DCEDC8'
      } else if (color === 'lime') {
        this.activeColor = '#F0F4C3'
        this.FormData.survey.color = '#F0F4C3'
      } else if (color === 'yellow') {
        this.activeColor = '#FFF9C4'
        this.FormData.survey.color = '#FFF9C4'
      } else if (color === 'amber') {
        this.activeColor = '#FFECB3'
        this.FormData.survey.color = '#FFECB3'
      } else if (color === 'orange') {
        this.activeColor = '#FFE0B2'
        this.FormData.survey.color = '#FFE0B2'
      } else if (color === 'deep-orange') {
        this.activeColor = '#FFCCBC'
        this.FormData.survey.color = '#FFCCBC'
      } else if (color === 'brown') {
        this.activeColor = '#D7CCC8'
        this.FormData.survey.color = '#D7CCC8'
      } else if (color === 'blue-grey') {
        this.activeColor = '#CFD8DC'
        this.FormData.survey.color = '#CFD8DC'
      } else if (color === 'grey') {
        this.activeColor = '#F5F5F5'
        this.FormData.survey.color = '#F5F5F5'
      }
    },
    closeModal() {
      this.dialog = false
    },
  },
  computed: {
    ...mapState(['originFormData', 'isSaved'])
  },
}
</script>

<style>
.container {
  margin-top: 50px;
  margin-bottom: 50px;
}
</style>
