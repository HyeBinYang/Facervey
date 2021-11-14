<template slot='cell' scope='props'>
  <div class="m-0" style="position:relative;">
    
    <v-list>
      <draggable>
      <v-card class="mb-4" v-for="(student, idx) in $store.state.Students" :key="idx">
        
        <v-list-item v-if="$store.state.Students" class="p-0">
          
          <v-list-item-content>

            <v-list-item-title>
              <v-icon
                @click="delete_student(idx,student.pk)"
                color="red"
                class="m-2"
                style="float: right;"
                >mdi-close
              </v-icon>
              <div
                :id="student.pk"
                v-if="student.flag"
                class="d-flex"
              >
                <div>
                  <v-icon x-large class="m-2" @click="student.flag=!student.flag">mdi-account</v-icon>
                </div>
                <div>
                  <div class="m-2">
                    <span>{{student.s_num}}</span>
                  </div>
                  <div class="m-2 d-flex justify-content-between w-100">
                    <div>{{student.y_num}}기</div>
                    <div>{{student.region}}</div>
                    <div>{{student.class_num}}반</div>
                    <div>{{student.name}}</div>
                    
                  </div>
                </div>
                
              </div>
              
              <div :id="student.pk" v-if="!student.flag" class="d-flex" style=" cursor:pointer;">
                <!-- <div @click="edit(student)"> -->
                <div @click="student.flag=!student.flag; edit(student);">
                  <v-icon x-large class="m-2">mdi-account</v-icon>
                </div>
                <div>
                  <!-- <div
                    class="d-flex justify-content-end"
                    @click="student.flag=!student.flag; edit(student);"
                  > -->
                    <!-- <v-icon
                      @click="delete_student(idx,student.pk)"
                      color="red"
                      class="m-2"
                      style="float: right;"
                    >mdi-close</v-icon> -->
                  <!-- </div> -->
                  <div style="width: 100%;">
                    <div class="m-2">
                      <v-text-field v-model="student.s_num" label="학번"></v-text-field>
                    </div>
                    <div class="d-flex align-items-center">
                      <v-text-field v-model="student.y_num" label="기수"></v-text-field>
                      <v-select :items="items" label="지역" v-model="student.region"></v-select>
                      <v-text-field v-model="student.class_num" label="반"></v-text-field>
                      <v-text-field v-model="student.name" label="이름"></v-text-field>
                      <div
                        class="d-flex justify-content-end"
                        @click="student.flag=!student.flag"
                      >
                        <v-icon @click="edit(student)" large color="blue">mdi-pencil</v-icon>
                      </div>
                      
                    </div>
                    
                  </div>
                  
                </div>
                
              </div>
            </v-list-item-title>
          </v-list-item-content>
        </v-list-item>

      </v-card>
      
    </draggable>  
    
    </v-list>
    
  </div>
</template>

<script>
import draggable from 'vuedraggable'
export default {

  components: {
    draggable,
  },

  data() {
    return {
      items: ["서울", "대전", "광주", "구미"],
    };
  },
  methods: {
    edit(student) {
      //이 student정보에서 s.flag만 뺀다.
      // this.student.flag = !student.flag;
      let newinfo = {
        class_num: student.class_num,
        name: student.name,
        pk: student.pk,
        region: student.region,
        s_num: student.s_num,
        y_num: student.y_num,
      };
      this.$store.dispatch("updateStudent", newinfo);
    },
    delete_student(idx, pk) {
      this.$store.state.Students.splice(idx, 1);
      this.$store.dispatch("deleteStudent", pk);
    },
    
  },
};
</script>

<style scoped>

</style>
