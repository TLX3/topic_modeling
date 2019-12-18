<template>
      <v-flex
        mt-5
        xs12
      >
        <v-data-table
                v-if="analyticsType === 'Dominant topic in each document'"
                :headers="headers1"
                :items="analyticsData[0]"
                hide-default-footer
                class="elevation-1"
        ></v-data-table>
        <v-data-table
                v-else-if="analyticsType === 'Topic distribution across companies'"
                :headers="headers2"
                :items="analyticsData[1]"
                hide-default-footer
                class="elevation-1"
        ></v-data-table>
        <v-data-table
                v-else-if="analyticsType === 'Most representative document for topic'"
                :headers="headers3"
                :items="analyticsData[2]"
                hide-default-footer
                class="elevation-1"
        ></v-data-table>
      </v-flex>
</template>

<script>
    export default {
        name: 'TopicAnalytics',
        props: ['analyticsData', 'analyticsType'],
        data: () => ({
            headers1: [
              { text: 'Document_No', value: 'Document_No' },
              { text: 'Dominant_Topic', value: 'Dominant_Topic' },
                { text: 'Keywords', value: 'Keywords' },
              { text: 'Topic_Percentage_Contrib', value: 'Topic_Percentage_Contrib' },
                { text: 'Document: Bag of Words', value: 'Text' },
            ],
            headers2: [
              { text: 'Dominant_Topic', value: 'Dominant_Topic' },
              { text: 'Num_Documents', value: 'Num_Documents' },
                { text: 'Percentage_Documents', value: 'Percentage_Documents' },
                { text: 'Topic_Keywords', value: 'Topic_Keywords' },
                { text: 'CIKs', value: 'CIKs'}
            ],
            headers3: [
              { text: 'Topic_Num', value: 'Topic_Num' },
              { text: 'Topic_Percentage_Contrib', value: 'Topic_Percentage_Contrib' },
                { text: 'Keywords', value: 'Keywords' },
                { text: 'Document: Bag of Words', value: 'Text' },
            ],
        }),
        mounted () {

        }
    };
</script>
