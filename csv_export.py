from nbgrader.plugins import ExportPlugin
from nbgrader.api import Gradebook, MissingEntry
import pandas as pd


class CsvExport(ExportPlugin):

    def get_columns(self, assignments):
        return [f"{a.name} | max_score: {int(a.max_score)}" for a in assignments]

    def get_assignments(self, gb: Gradebook):
        return sorted(filter(lambda x: not("-tg" in x.name), gb.assignments), key=lambda x: x.name)

    def export(self, gb: Gradebook) -> None:
        if self.to == "":
            dest = "grades.csv"
        else:
            dest = self.to

        self.log.info("Exporting grades to %s", dest)
        assignments = self.get_assignments(gb)
        data = []
        columns = ["Brukernavn"] + self.get_columns(assignments)

        for student in gb.students:
            row = [student.id]
            for assignment in assignments:
                score = None
                try:
                    submission = gb.find_submission(assignment.name, student.id)
                    score = submission.score
                except MissingEntry:
                    pass
                row.append(score)
            data.append(row)

        df = pd.DataFrame(data=data, columns=columns)

        fn = "list_of_students.csv"
        try:
            names = pd.read_csv(fn, sep=";")
        except FileNotFoundError:
            self.log.error(f"Could not find '{fn}', make sure the file exists!")
            names = pd.DataFrame(columns=["Etternavn", "Fornavn", "Brukernavn", "Student-Id"])

        df = names.merge(df, on="Brukernavn", how="outer")
        # df.sort_values(by=['Etternavn', 'Fornavn'], inplace=True)
        df.to_csv(dest, index=False, float_format='%.0f', sep=";", encoding="utf-8-sig")
