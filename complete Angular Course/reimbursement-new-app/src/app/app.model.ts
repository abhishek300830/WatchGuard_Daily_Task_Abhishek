export class UserDetailModel {
  public name: string;
  public designation: string;
  public employeeId: number;
  public reimbursements: ReimbursementModel[] = [];
}

export class ReimbursementModel {
  public id: number;
  public name: string;
  public amount: number;
  public type: string;
}
