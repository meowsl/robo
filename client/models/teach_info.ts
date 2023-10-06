export interface Teachers {
  id: number;
  photo: string | null;
  firstName: string;
  lastName: string;
  position: { name: string } | null;

  dateStart:string;
  dateEnd:string;
  studyPlace:string;
  studyFacult:string;
  studySpec:string;
  studyForm:string;
}


