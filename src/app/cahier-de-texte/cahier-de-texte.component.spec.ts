import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CahierDeTexteComponent } from './cahier-de-texte.component';

describe('CahierDeTexteComponent', () => {
  let component: CahierDeTexteComponent;
  let fixture: ComponentFixture<CahierDeTexteComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CahierDeTexteComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CahierDeTexteComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
