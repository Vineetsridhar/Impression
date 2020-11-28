export interface User {
  email: string;
  first_name: string;
  last_name: string;
  organization: string;
  descr: string;
  user_type: string;
  gen_link_1: string;
  gen_link_2: string;
  gen_link_3: string;
  image: string;
  doc: string;
}

export interface Group {
  user_id: number;
  group_name: string;
}
