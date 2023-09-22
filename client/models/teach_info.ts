export interface Teachers {
  id: number;
  photo: string | null;
  firstName: string;
  lastName: string;
  position: { name: string } | null;
}


export interface PackagesInfo {
  id: number;
  name: string;
  price: string;
  descript: string;
}